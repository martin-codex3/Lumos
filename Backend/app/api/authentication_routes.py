from fastapi import APIRouter

authentication_router = APIRouter()

@authentication_router.get("/create-account")
async def index():
    return {"message": "hey this is from the router group"}