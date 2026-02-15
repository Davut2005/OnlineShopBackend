from sqlmodel import Relationship, SQLModel, Field, String
from typing import Optional
from order import Order

class User(SQLModel, table = True):

    id: Optional[int] = Field(default=None ,primary_key=True, index= True)
    name: str = Field(String, index= True)
    email: str = Field(String, nullable= False, unique= True)

    orders: list["Order"] = Relationship( back_populates = "user" )