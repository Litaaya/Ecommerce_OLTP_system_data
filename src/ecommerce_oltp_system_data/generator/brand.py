from faker import Faker
from datetime import datetime

fake = Faker()

def generate_one_brand(brand_id: int) -> dict:
    return {
        "brand_id": brand_id,
        "brand_name": fake.unique.company(),
        "country": fake.country(),
        "created_at": fake.date_time_between(
            start_date = datetime(2024, 1, 1),
            end_date = datetime(2024, 12, 31),
        ),
    }


def is_valid_brand(brand: dict) -> bool:
    return (
        len(brand["brand_name"]) <= 100
        and len(brand["country"]) <= 50
    )


def generate_brands(count: int = 20) -> list[dict]:
    brands = []
    brand_id = 1

    while len(brands) < count:
        brand = generate_one_brand(brand_id)

        if is_valid_brand(brand):
            brands.append(brand)
            brand_id += 1

    return brands