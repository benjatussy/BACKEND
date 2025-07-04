from fastapi import FastAPI


app = FastAPI()

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