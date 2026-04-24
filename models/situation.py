from sqlmodel import SQLModel, Field
from sqlalchemy import ForeignKeyConstraint

class Situation(SQLModel, table=True):
    sit_id: int | None = Field(default=None, primary_key=True)
    play_id: int = Field() 
    game_id: str = Field()
    qtr: int | None = None
    qtr_seconds: int | None = None
    home_score: int | None = None
    away_score: int | None = None
    posteam: str | None = None
    yd_line: int | None = None
    down: int | None = None
    yds_to_go: int | None = None
    goal_to_go: bool | None = None
    hash: str | None = None

    __table_args__ = (
        ForeignKeyConstraint(
            ['game_id', 'play_id'],
            ['play.game_id','play.play_id']
        ),
    )

