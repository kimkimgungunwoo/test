import datetime

from pydantic import BaseModel

class Fish(BaseModel):
    dscription:str
    toxicity:bool
    fishtpye:str
    open_season:datetime
    close_season:datetime
    
    
    class Config:
        orm_mode =True