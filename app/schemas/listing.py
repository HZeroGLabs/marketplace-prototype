from pydantic import BaseModel
class ListingBase(BaseModel):
    title: str
    description: str
    price: float

class ListingCreate(ListingBase):
    owner_id: int

class Listing(ListingBase):
    id: int
    owner_id: int

    model_config = {
        "from_attributes": True
    }