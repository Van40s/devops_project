from fastapi import FastAPI
from car_discount import calculate_discount

app = FastAPI()


@app.get("/set_discount")
async def root(discount: float):
    updated_count = calculate_discount(discount=discount)

    return {
        "message": f"Prices updated with a {discount}% discount",
        "updated_count": updated_count,
    }
