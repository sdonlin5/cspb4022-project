from numpy import character
from sqlmodel import SQLModel, Field
from . import game

class Play(SQLModel, table=True):
    play_id: int | None=Field(default=None, primary_key=True)
    game_id: str = Field(foreign_key=game.game_id)
    pos_team: str
    qtr: int
    time_min: int
    time_sec: int
    yd_line: int
    hash: str
    down: int
    yds_to_go: int