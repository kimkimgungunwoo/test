from fastapi import APIRouter,Depends
from database import Session

from models import Fish
import fish_schema
from database import get_db





router=APIRouter(
    prefix="api/fish",
)

@router.get("/{fish_id}",response_model=fish_schema.Fish)
def get_fish(fish_id:int,db:Session=Depends(get_db)):
    fish_imformation=db.query(Fish).get(fish_id)
    return fish_imformation
    
   
    