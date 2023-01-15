from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Text,DateTime,TIMESTAMP,VARCHAR
from sqlalchemy.orm import relationship

from database import Base

class Fish(Base):
    __tablename__ = "Fish_Imformation"

    fish_id=Column(int,primary_key=True,index=True)
    fish_type=Column(VARCHAR,nullable=False)
    toxiciy=Column(Boolean,nullable=False)
    open_season=Column(DateTime,nullable=False)
    closed_season=Column(DateTime,nullable=False)
    fish_url=Column(VARCHAR,nullable=False)
    description=Column(VARCHAR,nullable=False)
    created_at=Column(DateTime,nullable=False)
    updated_at=Column(DateTime,nullable=False)
    is_active=Column(Boolean,nullable=False)
    
    


