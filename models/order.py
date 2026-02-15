from sqlmodel import SQLModel, Relationship, Field, String
from product import Product
from user import User
from order_item import OrderItem
from checkout import Checkouts

class Order(SQLModel, table=True):

    id: int = Field(default=None, primary_key=True, index= True)
    user_id: int = Field( nullable=False , foreign_key= "users.id" )

    user : "User" = Relationship( back_populates = "orders"  )
    products: list["Product"] = Relationship( back_populates="orders", link_model=OrderItem )
    checkouts: list["Checkouts"] = Relationship( back_populates = "order" )
    
    




    