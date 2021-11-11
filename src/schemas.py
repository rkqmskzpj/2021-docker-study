from typing import List, Optional


from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

