from sqlmodel import SQLModel, Relationship, Field, String
from product import Product
from user import User
from order import Order

class Checkout(SQLModel, table = True):

    id: int = Field( default=None, primary_key=True, index= True)
    user_id: int = Field( foreign_key="user.id" )
    order_id: int = Field(foreign_key="order.id", nullable= False, unique= True)
    amount : int

    user : "User" = Relationship( back_populates="checkouts" )
    order: "Order" = Relationship(back_populates="checkouts")