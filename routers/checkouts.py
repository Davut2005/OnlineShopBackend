from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.checkout import Checkout
from sqlmodel import select

router = APIRouter(
    prefix="/checkouts",
    tags=["checkouts"]
)

@router.post("/", response_model=Checkout)
async def addCheckout(
    checkout: Checkout,
    db : Session = Depends(get_db)
):
    db.add(checkout)
    db.commit()
    db.refresh(checkout)

    return checkout


@router.get("/{id}", response_model=Checkout)
async def getCheckout(
    id: int,
    db: Session = Depends(get_db)
):
    checkout = db.get(Checkout, id)

    if not checkout :
        raise HTTPException( status_code=404, detail="Checkout with this id not found" )

    return checkout


@router.get("/", response_model=list[Checkout])
async def getCheckouts(
    db: Session = Depends(get_db)
):
    checkouts = db.exec( select(Checkout) ).all()

    return checkouts


@router.put("/{id}", response_model=Checkout)
async def updateCheckout(
    id: int,
    checkout_data: Checkout,
    db: Session = Depends(get_db)
):
    checkout = db.get( Checkout, id )

    if not checkout :
        raise HTTPException( status_code=404, detail="Checkout with this id not found" )    

    for (field, value) in checkout_data.model_dump().items() :
        setattr(checkout, field, value)
    
    db.commit()
    db.refresh(checkout)

    return checkout


@router.delete("/{id}", response_model=Checkout)
async def deleteCheckout(
    id : int,
    db: Session = Depends(get_db)
):
    checkout = db.get(Checkout, id)

    if not checkout :
        raise HTTPException( status_code=404, detail="Checkout with this id not found" )
    
    db.delete(checkout)
    db.commit()

    return checkout