from fastapi import FastAPI


# change PYTHONDONTWRITEBYTECODE back to 0



app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World!"}

