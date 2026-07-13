from fastapi import FastAPI

app = FastAPI()

# Endpoint 1: The Root (Browser friendly)
@app.get("/")
def read_root():
    return {"message": "Welcome to my FlyRank backend!"}

# Endpoint 2: A status or data endpoint
@app.get("/status")
def read_status():
    return {"status": "online", "track": "backend-engineering-2026"}