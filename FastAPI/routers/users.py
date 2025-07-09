from fastapi import APIRouter,HTTPException
from pydantic import BaseModel



router = APIRouter(tags=["users"])
#python -m uvicorn routers.users:app --reload 
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

@router.get("/users.json")
async def usersjson():
    return [{"name": "Javierex", "lastname": "Quinde",  "age": 30, "url": "https://www.deepweb.com"},
            {"name": "MAK", "lastname": "OTO", "age": 16, "url": "https://www.youtube.com"}]

@router.get("/users")
async def users():
    return user_list

#Path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query
@router.get("/user/")
async def user(id: int):
    return search_user(id)

@router.post("/user/",response_model=User,status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    user_list.append(user)
    return user
        

@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
            
    
    if not found:
        return {"error": "El usuario no existe"}
    return {"message": "Usuario eliminado correctamente"}

#del elimina el elemento de la lista en la posición indicada, 
#liberando ese espacio y quitando el usuario de la lista.


@router.put("/user/")
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    
    if not found:
        return {"error": "El usuario no se ha actualizado"}
    return user
# Explicación:
# - enumerate(user_list): permite recorrer la lista user_list obteniendo tanto el índice (index) como el usuario (saved_user) en cada iteración.
# - index: es la posición actual en la lista, útil para modificar el elemento directamente.
# - found = False: se usa como bandera para saber si se encontró y actualizó el usuario.
# - found = True: se pone en True cuando se encuentra y actualiza el usuario.
# Si found sigue siendo False al final, significa que no se encontró el usuario y se devuelve un error.
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"error": "El usuario no existe"}