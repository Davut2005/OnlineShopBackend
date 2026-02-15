from sqlmodel import SQLModel, Relationship, String, Field
from product import Product
from order import Order
from typing import Optional

class OrderItem( SQLModel, table=True ):

    quantity: int
    order_id: int = Field( primary_key=True , nullable=False, foreign_key="order.id" )
    product_id: int = Field( primary_key=True , nullable=False, foreign_key="product.id" )

    order: "Order" = Relationship(back_populates="orderitems")
    product : "Product" = Relationship(back_populates="orderitems")