from pydantic import BaseModel

class CoffeeResponse(BaseModel):

    id: int

    name: str

    description: str

    image: str

    votes: int

    class Config:

        from_attributes = True