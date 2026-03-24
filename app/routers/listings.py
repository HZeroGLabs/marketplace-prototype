from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter

from app.db.database import get_db
from app.models.listings import Listing as ListingModel
from app.schemas.listing import Listing, ListingCreate
from app.utils.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/listings", response_model=Listing)
def create_listing(listing: ListingCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_listing = ListingModel(
        title=listing.title,
        description=listing.description,
        price=listing.price,
        owner_id=current_user.id
        )
    
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing

@router.get("/listings", response_model=List[Listing])
def get_listings(db: Session = Depends(get_db)):
    listings = db.query(ListingModel).all()
    return listings

@router.get("/listings/{listing_id}", response_model=Listing)
def get_listing(listing_id: int, db: Session = Depends(get_db)):
    listing = db.query(ListingModel).filter(ListingModel.id == listing_id).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing

@router.put("/listings/{listing_id}", response_model=Listing)
def update_listing(listing_id: int, listing: ListingCreate, db: Session = Depends(get_db)):
    db_listing = db.query(ListingModel).filter(ListingModel.id == listing_id).first()
    if not db_listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    
    db_listing.title = listing.title
    db_listing.description = listing.description
    db_listing.price = listing.price
    db.commit()
    db.refresh(db_listing)
    return db_listing

@router.delete("/listings/{listing_id}", response_model=Listing)
def delete_listing(listing_id: int, db: Session = Depends(get_db)):
    db_listing = db.query(ListingModel).filter(ListingModel.id == listing_id).first()
    if not db_listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    db.delete(db_listing)
    db.commit()
    return db_listing