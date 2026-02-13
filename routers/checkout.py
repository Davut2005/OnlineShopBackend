from fastapi import APIRouter

router = APIRouter(
    prefix="/checkouts",
    tags=["checkouts"]
)

@router.get
async def getCheckouts():
    pass

@router.post
async def addCheckout():
    pass

@router.put
async def updateCheckout():
    pass

@router.delete
async def deleteCheckout():
    pass