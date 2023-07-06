from pydantic import BaseModel

from typing import TypeVar
from pydantic import BaseModel
from pydantic.generics import BaseModel

M = TypeVar('M')

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        orm_mode = True
