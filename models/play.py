from sqlmodel import SQLModel, Field

class Play(SQLModel, table=True):
    game_id: str | None = Field(default=None, primary_key=True)
    play_id: int | None = Field(default=None, primary_key=True)
    qb_location: str | None = None
    num_te: int | None = None
    num_rb: int | None = None
    num_wr: int | None = None
    yds_gained: int | None = None
    rush_attempt: bool | None = None
    rush_touchdown: bool | None = None
    run_location: str | None = None
    run_gap: str | None = None
    pass_attempt: bool | None = None
    complete_pass: bool | None = None
    pass_touchdown: bool | None = None
    is_drop: bool | None = None
    interception: bool | None = None
    air_yards: int | None = None
    yards_after_catch: int | None = None
    pass_location: str | None = None
    route: str | None = None
    throw_away: bool | None = None
    play_action: bool | None = None
    screen_pass: bool | None = None
    qb_kneel: bool | None = None
    qb_spike: bool | None = None
    qb_dropback: bool | None = None
    qb_scramble: bool | None = None
    qb_sneak: bool | None = None
    trick_play: bool | None = None
    defenders_in_box: int | None = None
    n_pass_rushers: int | None = None
    n_blitzers: int | None = None
    was_pressure: bool | None = None
    sack: bool | None = None
    defense_man_zone_type: str | None = None
    defense_coverage_type: str | None = None
