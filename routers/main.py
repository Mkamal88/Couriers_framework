from fastapi import FastAPI

from routers import couriers, orders

app = FastAPI()


app.include_router(couriers.router)
app.include_router(orders.router)

