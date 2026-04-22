from sqlmodel import SQLModel, Field

class Schedule(SQLModel, Table=True):
    game_id: str | None = Field(default = None, primary_key=True)
    season: int 
    game_type: str 
    week: int
    away_team: str
    away_score: int | None = None
    home_team: str
    home_score: int | None = None