from fastapi import APIRouter
#python -m uvicorn products:router --reload 
router = APIRouter()

@router.get("/products")
async def products():
    return ["Product 1", "Product 2", "Product 3"]

