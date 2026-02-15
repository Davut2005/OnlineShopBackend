from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.user import User
from sqlmodel import SQLModel

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get
async def getUsers(
    id: int,
    db: Session = Depends(get_db)
):
    user = db.get(User, id)

    return user


@router.post
async def addUser():
    pass

@router.put
async def updateUser():
    pass

@router.delete
async def deleteUser():
    pass