from datetime import datetime
from faker import Faker

fake = Faker()

MAIN_CATEGORIES = [
    "Electronics",
    "Fashion",
    "Home & Living",
    "Beauty",
    "Sports",
]

SUB_CATEGORIES = {
    "Electronics": [
        "Mobile Phones",
        "Laptops",
        "Tablets",
        "Cameras",
    ],
    "Fashion": [
        "Men's Clothing",
        "Women's Clothing",
        "Shoes",
        "Accessories",
    ],
    "Home & Living": [
        "Furniture",
        "Kitchen",
        "Home Decor",
        "Bedding",
    ],
    "Beauty": [
        "Skincare",
        "Makeup",
        "Hair Care",
        "Fragrance",
    ],
    "Sports": [
        "Fitness",
        "Outdoor",
        "Cycling",
        "Sportswear",
    ],
}


def generate_one_category(
    category_id: int,
    category_name: str,
    level: int,
    parent_category_id: int | None,
    start_created_at: datetime,
) -> dict:

    return {
        "category_id": category_id,
        "category_name": category_name,
        "parent_category_id": parent_category_id,
        "level": level,
        "created_at": fake.date_time_between(
            start_date = start_created_at,
            end_date = datetime(2024, 12, 31),
        ),
    }


def is_valid_category(category: dict) -> bool:
    return (
        len(category["category_name"]) <= 100
        and category["level"] in {1, 2}
        and (
            (
                category["level"] == 1
                and category["parent_category_id"] is None
            )
            or
            (
                category["level"] == 2
                and category["parent_category_id"] is not None
            )
        )
    )


def generate_categories() -> list[dict]:
    categories = []
    main_category_ids = {}
    category_id = 1

    # Generate level 1 categories
    for category_name in MAIN_CATEGORIES:
        category = generate_one_category(
            category_id = category_id,
            category_name = category_name,
            level = 1,
            parent_category_id = None,
            start_created_at = datetime(2024, 1, 1),
        )

        if is_valid_category(category):
            categories.append(category)
            main_category_ids[category_name] = category_id
            category_id += 1

    # Generate level 2 categories
    for parent_name, subcategories in SUB_CATEGORIES.items():
        for category_name in subcategories:
            parent_category = next(
                category
                for category in categories
                if category["category_id"] == main_category_ids[parent_name]
            )

            category = generate_one_category(
                category_id=category_id,
                category_name=category_name,
                level=2,
                parent_category_id=main_category_ids[parent_name],
                start_created_at=parent_category["created_at"],
            )

            if is_valid_category(category):
                categories.append(category)
                category_id += 1

    return categories