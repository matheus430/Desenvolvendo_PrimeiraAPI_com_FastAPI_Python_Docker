from pydantic import BaseModel # type: ignore


class BaseSchema(BaseModel):
  class Config:
    extra = 'forbid'
    from_attributes = True