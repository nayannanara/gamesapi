from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        orm_mode = True
