from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db.database import get_db
from models.checkout import Checkouts

router = APIRouter(
    prefix="/checkouts",
    tags=["checkouts"]
)

@router.get
async def getCheckouts(
    id: int,
    db: Session = Depends(get_db)
):
    query = text("SELECT * FROM checkouts WHERE id == :id")

    return await db.execute(query, { "id" : id})


@router.post
async def addCheckout(
    checkout: dict,
    db: Session = Depends(get_db)
):
    pass

@router.put
async def updateCheckout():
    pass

@router.delete
async def deleteCheckout():
    pass