from datetime import date, timedelta, datetime
import random
from faker import Faker

fake = Faker()

def generate_one_seller(seller_id: int) -> dict:
    prefix = 50000

    join_date = fake.date_between(
        start_date = date(2024, 1, 1),
        end_date = date(2024, 12, 20),
    )

    created_at = fake.date_time_between(
        start_date = datetime.combine(
            join_date,
            datetime.min.time()
        ),
        end_date = datetime.combine(
            join_date + timedelta(days=random.randint(0, 10)),
            datetime.max.time()
        ),
    )

    return {
        "seller_id": seller_id,
        "seller_code": f"SEL-{prefix + seller_id}",
        "seller_name": fake.company(),
        "join_date": join_date,
        "seller_type": random.choice(["Official", "Marketplace"]),
        "rating": round(random.uniform(3, 5), 1),
        "country": "Vietnam",
        "created_at": created_at,
    }


def is_valid_seller(seller: dict) -> bool:
    return (
        len(seller["seller_code"]) <= 30
        and len(seller["seller_name"]) <= 150
        and seller["seller_type"] in {"Official", "Marketplace"}
        and 0 <= seller["rating"] <= 5
        and len(seller["country"]) <= 50
        and seller["created_at"].date() >= seller["join_date"]
    )


def generate_sellers(count: int = 50) -> list[dict]:
    sellers = []
    seller_id = 1

    while len(sellers) < count:
        seller = generate_one_seller(seller_id)

        if is_valid_seller(seller):
            sellers.append(seller)
            seller_id += 1

    return sellers