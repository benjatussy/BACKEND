from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/products"
                   , tags=["products"]
                   , responses={404: {"description": "Not found"}})



products_list = ["Product 1","Product 2","Product 3"
]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def product(id:int):
    return products_list[id]






# Permite ejecutar este archivo como una API independiente
app = FastAPI()
app.include_router(router)

#python -m uvicorn routers.products:app --reload