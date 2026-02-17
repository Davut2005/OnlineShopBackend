from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.product import Product
from sqlmodel import select

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.post("/", response_model=Product)
async def addProduct(
    product: Product,
    db : Session = Depends(get_db)
):
    db.add(product)
    db.commit()
    db.refresh(product)

    return product


@router.get("/{id}", response_model=Product)
async def getProduct(
    id: int,
    db: Session = Depends(get_db)
):
    product = db.get(Product, id)

    if not product :
        raise HTTPException( status_code=404, detail="Product with this id not found" )

    return product


@router.get("/", response_model=list[Product])
async def getProducts(
    db: Session = Depends(get_db)
):
    products = db.exec( select(Product) ).all()

    return products


@router.put("/{id}", response_model=Product)
async def updateProduct(
    id: int,
    product_data: Product,
    db: Session = Depends
):
    product = db.get( Product, id )

    if not product :
        raise HTTPException( status_code=404, detail="Product with this id not found" )    

    for (field, value) in product_data.model_dump().items() :
        setattr(product, field, value)
    
    db.commit()
    db.refresh(product)

    return product


@router.delete("/{id}", response_model=Product)
async def deleteProduct(
    id : int,
    db: Session = Depends(get_db)
):
    product = db.get(Product, id)

    if not product :
        raise HTTPException( status_code=404, detail="Product with this id not found" )
    
    db.delete(product)
    db.commit()

    return product