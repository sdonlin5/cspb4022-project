from sqlmodel import SQLModel, Field

class Situation(SQLModel, table=True):
    sit_id: int | None = Field(default=None, primary_key=True)
    play_id: int = Field(foreign_key="play.play_id") 
    game_id: str = Field(foreign_key="play.game_id")
    qtr: int | None = None
    qtr_seconds: int | None = None
    posteam: str | None = None
    yd_line: int | None = None
    down: int | None = None
    yds_to_go: int | None = None
    goal_to_go: bool | None = None
    hash: str | None = None