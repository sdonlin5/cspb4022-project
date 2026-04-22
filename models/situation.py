from sqlmodel import SQLModel, Field

class Situation(SQLModel, table=True):
    sit_id: int = Field(default = None, primary_key=True)
    play_id: int = Field(foreign_key=True)
    game_id: int = Field(foreign_key=True)
    qtr: int | None = None
    minutes: int | None = None
    seconds: int | None = None
    posteam: str  | None = None
    yd_line: int | None = None
    down: int | None = None
    ydstogo: int | None = None
    goal_to_go: bool | None = None
    hash_side: str | None = None