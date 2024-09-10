from fastapi import APIRouter
from model.map import Map
import service.map as service


router = APIRouter(prefix = "/map")

@router.get("")
@router.get("/")
def get_all()->Map:
    return service.get_one("test")
