from datetime import datetime, time
import random
from faker import Faker

fake = Faker()

def generate_promotion_products(
    promotions: list[dict],
    products: list[dict],
    count: int = 500,
) -> list[dict]:

    promotion_products = []
    promo_product_id = 1

    # Prevent duplicate (promotion_id, product_id)
    used_pairs = set()

    # Fix one business target for each category/seller promotion
    promotion_targets = {}

    product_category_ids = list({
        product["category_id"]
        for product in products
    })

    product_seller_ids = list({
        product["seller_id"]
        for product in products
    })

    for promotion in promotions:
        promotion_type = promotion["promotion_type"]

        if promotion_type == "category":
            promotion_targets[promotion["promotion_id"]] = {
                "category_id": random.choice(product_category_ids)
            }

        elif promotion_type == "seller":
            promotion_targets[promotion["promotion_id"]] = {
                "seller_id": random.choice(product_seller_ids)
            }

        else:
            promotion_targets[promotion["promotion_id"]] = None

    while len(promotion_products) < count:
        promotion = random.choice(promotions)
        promotion_id = promotion["promotion_id"]
        promotion_type = promotion["promotion_type"]

        target = promotion_targets[promotion_id]

        if promotion_type == "category":
            candidate_products = [
                product
                for product in products
                if product["category_id"] == target["category_id"]
            ]

        elif promotion_type == "seller":
            candidate_products = [
                product
                for product in products
                if product["seller_id"] == target["seller_id"]
            ]

        else:
            candidate_products = products

        if promotion["discount_type"] == "fixed_amount":
            candidate_products = [
                product
                for product in candidate_products
                if product["price"] > promotion["discount_value"]
            ]

        if not candidate_products:
            continue

        product = random.choice(candidate_products)

        pair = (
            promotion_id,
            product["product_id"],
        )

        if pair in used_pairs:
            continue

        start_datetime = max(
            promotion["created_at"],
            product["created_at"],
        )

        end_datetime = datetime.combine(
            promotion["end_date"],
            time.max,
        )

        if start_datetime > end_datetime:
            continue

        created_at = fake.date_time_between(
            start_date=start_datetime,
            end_date=end_datetime,
        )

        promotion_product = {
            "promo_product_id": promo_product_id,
            "promotion_id": promotion_id,
            "product_id": product["product_id"],
            "created_at": created_at,
        }

        promotion_products.append(promotion_product)
        used_pairs.add(pair)

        promo_product_id += 1

    return promotion_products