from fastapi import FastAPI
from car_discount import calculate_discount, get_available_cars

app = FastAPI(
    title="Car Discount API",
    description="This API allows you to set discounts on car prices.",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    docs_url="/docs",  # You can change this path if needed
    redoc_url="/redoc",  # You can change this path if needed
)


@app.get("/set_discount")
async def root(discount: float):
    updated_count = calculate_discount(discount=discount)

    return {
        "message": f"Prices updated with a {discount}% discount",
        "updated_count": updated_count,
    }


@app.get("/get_cars")
async def root():
    cars = get_available_cars()

    return {"available cars": cars}


@app.get("/")
async def root():
    return {"message": "Hello World"}
