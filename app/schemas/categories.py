from pydantic import BaseModel, Field


class CreateCategory(BaseModel):
    name: str
    description: str


class UpdateCategory(CreateCategory):
    ident: int = Field(..., gt=0)
