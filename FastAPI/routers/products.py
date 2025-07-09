from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/products"
                   , tags=["products"]
                   , responses={404: {"description": "Not found"}})

@router.get("/")
async def products():
    return products_list

products_list = [{
    "Product 1",
    "Product 2",
    "Product 3"
}
]

@router.get("/{id}")
async def products():
    return products_list[id]
# Permite ejecutar este archivo como una API independiente
app = FastAPI()
app.include_router(router)

#python -m uvicorn routers.products:app --reload