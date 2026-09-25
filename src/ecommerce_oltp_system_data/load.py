from pathlib import Path
import os
import psycopg
from dotenv import load_dotenv
from ecommerce_oltp_system_data.loader.load_csv import load_csv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"


def main():
    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    try:
        load_csv(
            connection,
            "brand",
            DATA_DIR / "brand.csv",
        )

        load_csv(
            connection,
            "category",
            DATA_DIR / "category.csv",
        )

        load_csv(
            connection,
            "seller",
            DATA_DIR / "seller.csv",
        )

        load_csv(
            connection,
            "customer",
            DATA_DIR / "customer.csv",
        )

        load_csv(
            connection,
            "promotion",
            DATA_DIR / "promotion.csv",
        )

        load_csv(
            connection,
            "product",
            DATA_DIR / "product.csv",
        )

        load_csv(
            connection,
            "promotion_product",
            DATA_DIR / "promotion_product.csv",
        )

        connection.commit()
        print("All CSV files loaded successfully.")

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

if __name__ == "__main__":
    main()