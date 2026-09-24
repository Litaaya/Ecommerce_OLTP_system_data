from datetime import datetime
import random
from faker import Faker

fake = Faker()

def generate_one_customer(customer_id: int) -> dict:
    return {
        "customer_id": customer_id,
        "customer_name": fake.name(),
        "email": fake.unique.email(),
        "phone": fake.unique.phone_number(),
        "gender": random.choice(["Male", "Female"]),
        "address": fake.address(),
        "city": fake.city(),
        "created_at": fake.date_time_between(
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 12, 31),
        ),
    }


def is_valid_customer(customer: dict) -> bool:
    return (
        len(customer["customer_name"]) <= 150
        and len(customer["email"]) <= 150
        and len(customer["phone"]) <= 20
        and customer["gender"] in {"Male", "Female"}
        and len(customer["address"]) <= 255
        and len(customer["city"]) <= 100
    )


def generate_customers(count: int = 30_000) -> list[dict]:
    customers = []
    customer_id = 1

    while len(customers) < count:
        customer = generate_one_customer(customer_id)

        if is_valid_customer(customer):
            customers.append(customer)
            customer_id += 1

    return customers