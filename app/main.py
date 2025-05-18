from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/data")
def read_root():
    return {"data": "rankbooster"}
