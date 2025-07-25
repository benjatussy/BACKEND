from fastapi import Depends, HTTPException, status, APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter()

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool 
    
class UserDB(User):
    password: str
    
users_db = {
    "GASTON": {
        "username": "gaston",
        "fullname": "gastonto",
        "email": "gaston@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "siu": {
        "username": "CRISHTIANO",
        "fullname": "CRISTIANO RONALDO",
        "email": "cris_7@gmail.com",
        "disabled": True,
        "password": "1234567"
    }
}

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas", 
            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inhabilitado")
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:  
        raise HTTPException(status_code=400, detail="El usuario no es correcto")
    
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")
    
    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

@router.get("/users")
async def get_users():
    return [{"username": "test"}]
