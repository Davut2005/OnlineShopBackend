from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from category import Category

class Product (Base):
    __tablename__ = "products"

    id = Column( Integer, primary_key=True, index= True )
    name = Column( String, index=True )
    category_name = Column( String, ForeignKey("categories.name") )

    category = relationship("Category", back_populates="product")

