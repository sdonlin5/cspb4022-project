import streamlit as st
import polars as pl
import plotly.express as px
from database.db import sync_engine

@st.cache_data
def load_data(team):
    query = f"""
    SELECT p.*, s.down, s.yds_to_go, s.posteam
    FROM play p
    JOIN situation s ON p.play_id = s.play_id AND p.game_id = s.game_id
    WHERE s.posteam = '{team}'
    """
    return pl.read_database(query, connection=sync_engine)

st.set_page_config(layout="wide", page_title="NFL Tactical Tendencies")
st.sidebar.title("Filters")
selected_team = st.sidebar.selectbox("Team", ["ARI", "NO", "SEA", "KC", "BUF"])
df = load_data(selected_team)

st.title(f"🏈 {selected_team} Tactical Analysis")
task = st.radio("Task Selection", ["Run Tendency", "Passing Completion", "Pass Coverage"], horizontal=True)
st.divider()

if task == "Run Tendency":
    # Filters
    c1, c2, c3 = st.columns(3)
    down = c1.selectbox("Down", [1, 2, 3, 4])
    dist = c2.selectbox("Distance Category", ["0-3yds", "4-6yds", "7+yds"])
    pers = c3.selectbox("Personnel", ["10", "11", "12", "21", "22"])

    # Processing
    viz_df = df.filter((pl.col('rush_attempt') == True) & (pl.col('run_location').is_in(['left', 'right'])))
    viz_df = viz_df.with_columns(
        dist_cat = pl.when(pl.col('yds_to_go') <= 3).then(pl.lit("0-3yds"))
                     .when(pl.col('yds_to_go') <= 6).then(pl.lit("4-6yds"))
                     .otherwise(pl.lit("7+yds")),
        personnel = (pl.col('num_rb').cast(pl.Utf8) + pl.col('num_te').cast(pl.Utf8))
    ).filter((pl.col('down') == down) & (pl.col('dist_cat') == dist) & (pl.col('personnel') == pers))
    
    viz_df = viz_df.with_columns(path = pl.col('run_location') + " " + pl.col('run_gap').fill_null("end"))
    
    order = ["left end", "left tackle", "left guard", "right guard", "right tackle", "right end"]
    fig = px.bar(viz_df['path'].value_counts().to_pandas(), x="path", y="count", 
                 category_orders={"path": order}, color="count", color_continuous_scale="Reds")
    st.plotly_chart(fig, use_container_width=True)

elif task == "Passing Completion":
    viz_df = df.filter((pl.col('pass_attempt') == True) & (pl.col('pass_location').is_not_null()))
    viz_df = viz_df.with_columns(
        depth = pl.when(pl.col('air_yards') <= 10).then(pl.lit("0-10yds"))
                  .when(pl.col('air_yards') <= 25).then(pl.lit("11-25yds"))
                  .otherwise(pl.lit("25+yds"))
    )
    stats = viz_df.group_by(['pass_location', 'depth']).agg(rate = pl.col('complete_pass').mean() * 100)
    fig = px.density_heatmap(stats.to_pandas(), x="pass_location", y="depth", z="rate", text_auto=".1f",
                             category_orders={"pass_location": ["left", "middle", "right"], 
                                              "depth": ["25+yds", "11-25yds", "0-10yds"]},
                             color_continuous_scale="RdYlGn")
    st.plotly_chart(fig, use_container_width=True)

else: # Pass Coverage
    c1, c2 = st.columns(2)
    down_v3 = c1.selectbox("Down", [1, 2, 3, 4], key="v3d")
    dist_v3 = c2.slider("Distance Threshold", 1, 20, 10)
    
    viz_df = df.filter((pl.col('down') == down_v3) & (pl.col('yds_to_go') <= dist_v3))
    viz_df = viz_df.filter(pl.col('defense_man_zone_type').is_not_null()).with_columns(
        coverage = pl.col('defense_man_zone_type') + " (" + pl.col('defense_coverage_type') + ")"
    )
    fig = px.bar(viz_df['coverage'].value_counts().sort("count").to_pandas(), x="count", y="coverage", orientation='h')
    st.plotly_chart(fig, use_container_width=True)