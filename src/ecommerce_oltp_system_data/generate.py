import csv
from datetime import date, datetime
from pathlib import Path

from ecommerce_oltp_system_data.generator.brand import generate_brands
from ecommerce_oltp_system_data.generator.seller import generate_sellers
from ecommerce_oltp_system_data.generator.customer import generate_customers
from ecommerce_oltp_system_data.generator.category import generate_categories
from ecommerce_oltp_system_data.generator.promotion import generate_promotions
from ecommerce_oltp_system_data.generator.product import generate_products
from ecommerce_oltp_system_data.generator.promotion_product import generate_promotion_products

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

def serialize_value(value):
    if isinstance(value, datetime):
        return value.isoformat(sep=" ")

    if isinstance(value, date):
        return value.isoformat()

    return value

def export_to_csv(data: list[dict], filename: str) -> None:

    if not data:
        return

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    file_path = DATA_DIR / filename

    with file_path.open(mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=data[0].keys(),
        )

        writer.writeheader()

        for row in data:
            serialized_row = {
                key: serialize_value(value)
                for key, value in row.items()
            }

            writer.writerow(serialized_row)

    print(
        f"{filename}: "
        f"{len(data):,} rows exported"
    )


def main():
    brands = generate_brands()
    sellers = generate_sellers()
    customers = generate_customers()
    categories = generate_categories()
    promotions = generate_promotions()

    products = generate_products(
        brands=brands,
        categories=categories,
        sellers=sellers,
    )

    promotion_products = generate_promotion_products(
        promotions=promotions,
        products=products,
    )

    export_to_csv(
        brands,
        "brand.csv",
    )

    export_to_csv(
        sellers,
        "seller.csv",
    )

    export_to_csv(
        customers,
        "customer.csv",
    )

    export_to_csv(
        categories,
        "category.csv",
    )

    export_to_csv(
        promotions,
        "promotion.csv",
    )

    export_to_csv(
        products,
        "product.csv",
    )

    export_to_csv(
        promotion_products,
        "promotion_product.csv",
    )

if __name__ == "__main__":
    main()