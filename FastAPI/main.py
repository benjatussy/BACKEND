from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

#python -m uvicorn main:app --reload 