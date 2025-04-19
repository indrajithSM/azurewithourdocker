from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Deployed without Docker!"}

@app.get("/ping")
def ping():
    return {"status": "alive"}
