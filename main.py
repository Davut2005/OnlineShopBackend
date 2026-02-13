from fastapi import FastAPI
from routers import orders, users, products, checkouts 

app = FastAPI()

app.include_router( orders.router )
app.include_router( users.router )
app.include_router( checkouts.router )
app.include_router( orders.router )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
