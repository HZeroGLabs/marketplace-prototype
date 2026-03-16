from pydantic import BaseModel
class ListingBase(BaseModel):
    title: str
    description: str
    price: float

class ListingCreate(ListingBase):
    pass

class Listing(ListingBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True