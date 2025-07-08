from fastapi import FastAPI
from db import init_db
from routes import auth, transactions
app = FastAPI()


app.include_router(auth.router)
app.include_router(transactions.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
def startup():
    init_db()