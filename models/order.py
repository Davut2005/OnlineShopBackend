from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from product import Product
from user import User

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index= True)
    user_id = Column(Integer, ForeignKey( "users.id" ))
    

class OrderItem(Base):
    __tablename__ = "order_items"

    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable= False)
    order_id = Column( Integer )



    