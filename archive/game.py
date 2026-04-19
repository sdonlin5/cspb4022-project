from sqlmodel import SQLModel, Field


class Game(SQLModel, table=True):
    game: str | None = Field(default=None, primary_key=True) # uses the nflreadpy game id as the primary key
    season: int
    season_type: str
    week: int
    home_team: str 
    away_team: str