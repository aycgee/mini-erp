from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def calisiyor():
    return {"mesaj": "çalışıyor"}