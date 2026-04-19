from sqlalchemy import ForeignKey
from sqlmodel import SQLModel, Field
from . import play

class Playcall(SQLModel, table=True): 
    id: int | None=Field(default=None, primary_key=True)
    play_id: int = Field(foreign_key=play.play_id)
    run_side: str
    run_gap: str
    rush_yds: int
    pass_loc: str
    pass_length: str
    pass_air_yds: int
    pass_yac: int
    interception: bool
    throw_away: bool 
    