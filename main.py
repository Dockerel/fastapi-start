from fastapi import FastAPI

app = FastAPI()

from fastapi.responses import FileResponse


@app.get("/")
def home():
    return FileResponse("index.html")


# @app.get("/")
# async def home():
#     await db.load()
#     return FileResponse("db.html")


from pydantic import BaseModel


class Model(BaseModel):
    name: str
    phone: int


@app.post("/send")
def send(data: Model):
    print(data)
    return "전송완료"
