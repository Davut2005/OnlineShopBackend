from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from product import Product
from user import User

class Checkouts(Base):
    __tablename__ = "checkouts"

    id = Column(Integer, primary_key=True, index= True)
    user_id = Column(Integer)
    order_id = Column(Integer, nullable= False, unique= True)
    amount = Column(Integer)