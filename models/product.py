from sqlmodel import SQLModel, Relationship, Field, Integer, String
from typing import Optional, TYPE_CHECKING
from .order_item import OrderItem

if TYPE_CHECKING :
    from .category import Category
    from .order import Order

class Product (SQLModel, table=True):


    id: Optional[int] = Field( default=None , primary_key=True, index= True )
    name: str = Field( String, index=True )
    category_name: str = Field( String, foreign_key="categories.name" )

    category: "Category" = Relationship( back_populates="products")
    orders: list["Order"] = Relationship( back_populates="products", link_model=OrderItem )



