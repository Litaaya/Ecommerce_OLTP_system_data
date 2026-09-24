from datetime import date, datetime, timedelta
import random
from faker import Faker

fake = Faker()

PROMOTION_NAMES = [
    "New Year Sale",
    "Lunar New Year Sale",
    "Valentine Sale",
    "March Mega Sale",
    "Summer Sale",
    "Mid-Year Sale",
    "Back To School Sale",
    "Weekend Sale",
    "Flash Sale",
    "Payday Sale",
]


def generate_one_promotion(promotion_id: int) -> dict:
    prefix = 70000

    created_at = fake.date_time_between(
        start_date = datetime(2024, 12, 1),
        end_date = datetime(2025, 4, 20),
    )

    start_boundary = max(
        created_at.date(),
        date(2025, 1, 1),
    )

    start_date = fake.date_between(
        start_date=start_boundary,
        end_date=date(2025, 4, 30),
    )

    end_date = start_date + timedelta(
        days = random.randint(7, 30)
    )

    discount_type = random.choice([
        "percentage",
        "fixed_amount",
    ])

    if discount_type == "percentage":
        discount_value = round(
            random.uniform(5, 50),
            2,
        )
    else:
        discount_value = round(
            random.uniform(10_000, 500_000),
            2,
        )

    return {
        "promotion_id": promotion_id,
        "promotion_code": f"PROMO-{prefix + promotion_id}",
        "promotion_name": random.choice(PROMOTION_NAMES),
        "promotion_type": random.choice([
            "product",
            "category",
            "seller",
            "flash_sale",
        ]),
        "discount_type": discount_type,
        "discount_value": discount_value,
        "start_date": start_date,
        "end_date": end_date,
        "created_at": created_at,
    }


def is_valid_promotion(promotion: dict) -> bool:
    return (
        len(promotion["promotion_code"]) <= 30
        and len(promotion["promotion_name"]) <= 100
        and len(promotion["promotion_type"]) <= 50
        and promotion["discount_type"] in {
            "percentage",
            "fixed_amount",
        }
        and promotion["discount_value"] > 0
        and (
            promotion["discount_type"] == "fixed_amount"
            or promotion["discount_value"] <= 100
        )
        and promotion["start_date"] >= promotion["created_at"].date()
        and promotion["end_date"] >= promotion["start_date"]
    )


def generate_promotions(count: int = 30) -> list[dict]:
    promotions = []
    promotion_id = 1

    while len(promotions) < count:
        promotion = generate_one_promotion(promotion_id)

        if is_valid_promotion(promotion):
            promotions.append(promotion)
            promotion_id += 1

    return promotions