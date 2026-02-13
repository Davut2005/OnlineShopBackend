from fastapi import APIRouter

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get
async def getOrders():
    pass

@router.post
async def addOrder():
    pass

@router.put
async def updateOrder():
    pass

@router.delete
async def deleteOrder():
    pass