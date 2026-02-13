from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from product import Product

class Category (Base):
    __tablename__ = "categories"

    id = Column( Integer, primary_key= True, index= True )
    name = Column( String, index= True )

    product = relationship("Product", back_populates="category")
