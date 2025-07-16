from fastapi import FastAPI
from routers import products, users, basic_auth_users
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(basic_auth_users.router)

@app.get("/")
async def root():
    return {"message": "Hello, javierex!"}

#URL LOCAL http://127.0.0.1:8000 

@app.get("/url")
async def url():
    return {"url_curso": "https://www.youtube.com"}

#URL LOCAL http://127.0.0.1:8000/url


#documentation http://127.0.0.1:8000/docs
#documentation http://127.0.0.1:8000/redoc
#python -m uvicorn main:app --reload 