from sqlmodel import SQLModel, Relationship, Field, Integer, String
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING :
    from .product import Product


class Category (SQLModel, table=True):

    id: int = Field( default=None, primary_key= True, index= True )
    name: str = Field( String, index= True )

    products: list["Product"] = Relationship( back_populates="category")




