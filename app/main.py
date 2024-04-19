from typing import Union

from fastapi import FastAPI

import requests # type: ignore

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&apiKey=81nz1Dp5KDRbFPb9o62GFt5I0x49X61cHXhYNOH5&returnType=json"

    contents = requests.get(URL).text
    return {"message": contents}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q":q}