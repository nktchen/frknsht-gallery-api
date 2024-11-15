from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def home():
    return {"data": "Hello World"}


@app.get("/img")
async def img():
    return FileResponse("output_img/output_page_3_1.png")

