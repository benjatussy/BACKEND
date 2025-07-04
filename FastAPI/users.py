from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#python -m uvicorn users:app --reload 
class User(BaseModel):
    id: int
    name: str
    lastname: str
    age: int
    url: str

user_list = [
    User(id=1, name="Javierex", lastname="Quinde", age=30, url="https://www.deepweb.com"),
    User(id=2, name="MAK", lastname="OTO", age=16, url="https://www.youtube.com")
]

@app.get("/users.json")
async def usersjson():
    return [{"name": "Javierex", "lastname": "Quinde",  "age": 30, "url": "https://www.deepweb.com"},
            {"name": "MAK", "lastname": "OTO", "age": 16, "url": "https://www.youtube.com"}]

@app.get("/users")
async def users():
    return user_list

#Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query
@app.get("/user/")
async def user(id: int):
    return search_user(id)
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"error": "El usuario no existe"}