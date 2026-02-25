from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.user import User
from sqlmodel import SQLModel, select

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=User)
async def addUser(
    user: User,
    db : Session = Depends(get_db)
):
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.get("/{id}", response_model=User)
async def getUser(
    id: int,
    db: Session = Depends(get_db)
):
    user = db.get(User, id)

    if not user :
        raise HTTPException( status_code=404, detail="User with this id not found" )

    return user


@router.get("/", response_model=list[User])
async def getUser(
    db: Session = Depends(get_db)
):
    users = db.exec( select(User) ).all()

    return users


@router.put("/{id}", response_model=User)
async def updateUser(
    id: int,
    user_data: User,
    db: Session = Depends(get_db)
):
    user = db.get( User, id )

    if not user :
        raise HTTPException( status_code=404, detail="User with this id not found" )    

    for (field, value) in user_data.model_dump().items() :
        setattr(user, field, value)
    
    db.commit()
    db.refresh(user)

    return user


@router.delete("/{id}", response_model=User)
async def deleteUser(
    id : int,
    db: Session = Depends(get_db)
):
    user = db.get(User, id)

    if not user :
        raise HTTPException( status_code=404, detail="User with this id not found" )
    
    db.delete(user)
    db.commit()

    return user