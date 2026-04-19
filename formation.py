from numpy import character
from sqlmodel import SQLModel, Field
import play


class Formation(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    play_id: int = Field(foreign_key=play.play_id)
    formation: str
    rb: int
    fb: int 
    te: int
    wr: int




