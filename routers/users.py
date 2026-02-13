from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get
async def getUsers():
    pass

@router.post
async def addUser():
    pass

@router.put
async def updateUser():
    pass

@router.delete
async def deleteUser():
    pass