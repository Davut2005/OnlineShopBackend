from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.product import Product

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get
async def getProducts(
    id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == id).first()

    return product

@router.post
async def addProduct():
    pass

@router.put
async def updateProduct():
    pass

@router.delete
async def deleteProduct():
    pass