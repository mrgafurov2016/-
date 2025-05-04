# hotels/schemas.py
from pydantic import BaseModel

class RoomCreate(BaseModel):
    number: str
    floor: int
    capacity: int

class RoomOut(RoomCreate):
    id: int

    class Config:
        orm_mode = True