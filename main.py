from fastapi import (FastAPI)
import random

app = FastAPI()

#http://127.0.0.1:8000/
@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

#http://127.0.0.1:8000/teste1

@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(1, 1000)}

