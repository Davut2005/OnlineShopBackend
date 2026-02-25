from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.order import Order
from sqlmodel import select

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.post("/", response_model=Order)
async def addOrder(
    order: Order,
    db : Session = Depends(get_db)
):
    db.add(order)
    db.commit()
    db.refresh(order)

    return order


@router.get("/{id}", response_model=Order)
async def getOrder(
    id: int,
    db: Session = Depends(get_db)
):
    order = db.get(Order, id)

    if not order :
        raise HTTPException( status_code=404, detail="Order with this id not found" )

    return order


@router.get("/", response_model=list[Order])
async def getOrders(
    db: Session = Depends(get_db)
):
    orders = db.exec( select(Order) ).all()

    return orders


@router.put("/{id}", response_model=Order)
async def updateOrder(
    id: int,
    order_data: Order,
    db: Session = Depends(get_db)
):
    order = db.get( Order, id )

    if not order :
        raise HTTPException( status_code=404, detail="Order with this id not found" )    

    for (field, value) in order_data.model_dump().items() :
        setattr(order, field, value)
    
    db.commit()
    db.refresh(order)

    return order


@router.delete("/{id}", response_model=Order)
async def deleteOrder(
    id : int,
    db: Session = Depends(get_db)
):
    order = db.get(Order, id)

    if not order :
        raise HTTPException( status_code=404, detail="Order with this id not found" )
    
    db.delete(order)
    db.commit()

    return order