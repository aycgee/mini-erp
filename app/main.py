from fastapi import FastAPI

from app.routers import urunler

app = FastAPI()
app.include_router(urunler.router)


@app.get("/")
def calisiyor():
    return {"mesaj": "çalışıyor"}