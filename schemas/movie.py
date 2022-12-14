from datetime import date, datetime, timedelta
from typing import List, Union
from pydantic import BaseModel, Field

from schemas.artist import GetArtist
from schemas.comment import GetComment


class MovieBase(BaseModel):
    name: str = Field(example="yolo king")
    release_date: str = Field(
        example=str(datetime.now() - timedelta(days=3*365))
    )


class PostMovie(MovieBase):
    director_person_id: Union[str, None]
    actor_person_id: Union[str, None]
    actress_person_id: Union[str, None]


class GetMovie(MovieBase):
    id: str
    comments: List[GetComment]
    director_person: GetArtist
    actor_person: GetArtist
    actress_person: GetArtist

    class Config:
        orm_mode = True
