from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.order import Order

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get
async def getOrders(
    id: int,
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(Order.id == id).first()

    return order

@router.post
async def addOrder():
    pass

@router.put
async def updateOrder():
    pass

@router.delete
async def deleteOrder():
    pass