from typing import List;
from pydantic import BaseModel, conint;


class Map(BaseModel):
    data : List[List[conint(ge=0, le=3)]]