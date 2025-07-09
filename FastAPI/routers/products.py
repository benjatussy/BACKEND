from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/products")
async def products():
    return ["Product 1", "Product 2", "Product 3"]



# Permite ejecutar este archivo como una API independiente
app = FastAPI()
app.include_router(router)

#python -m uvicorn routers.products:app --reload