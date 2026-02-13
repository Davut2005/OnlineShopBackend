from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get
async def getProducts():
    pass

@router.post
async def addProduct():
    pass

@router.put
async def updateProduct():
    pass

@router.delete
async def deleteProduct():
    pass