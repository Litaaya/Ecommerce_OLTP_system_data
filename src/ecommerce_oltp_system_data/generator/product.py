from datetime import datetime
import random
from faker import Faker

fake = Faker()

PRODUCT_CONFIG = {
    "Mobile Phones": {
        "types": [
            "Smartphone",
            "5G Smartphone",
            "Pro Smartphone",
            "Gaming Smartphone",
            "Foldable Smartphone",
        ],
        "variants": [
            "128GB",
            "256GB",
            "512GB",
            "1TB",
            "256GB Dual SIM",
        ],
        "price_range": (3_000_000, 40_000_000),
    },

    "Laptops": {
        "types": [
            "Ultrabook",
            "Gaming Laptop",
            "Business Laptop",
            "Notebook",
            "Creator Laptop",
        ],
        "variants": [
            "8GB RAM",
            "16GB RAM",
            "32GB RAM",
            "512GB SSD",
            "1TB SSD",
        ],
        "price_range": (8_000_000, 60_000_000),
    },

    "Tablets": {
        "types": [
            "Tablet",
            "Pro Tablet",
            "Gaming Tablet",
            "Kids Tablet",
            "Business Tablet",
        ],
        "variants": [
            "64GB",
            "128GB",
            "256GB",
            "WiFi",
            "5G",
        ],
        "price_range": (3_000_000, 30_000_000),
    },

    "Cameras": {
        "types": [
            "Mirrorless Camera",
            "DSLR Camera",
            "Action Camera",
            "Compact Camera",
            "Instant Camera",
        ],
        "variants": [
            "Body Only",
            "18-55mm Kit",
            "4K",
            "20MP",
            "24MP",
        ],
        "price_range": (2_000_000, 50_000_000),
    },

    "Men's Clothing": {
        "types": [
            "T-Shirt",
            "Polo Shirt",
            "Jacket",
            "Jeans",
            "Casual Shirt",
        ],
        "variants": [
            "Size S",
            "Size M",
            "Size L",
            "Size XL",
            "Size XXL",
        ],
        "price_range": (100_000, 3_000_000),
    },

    "Women's Clothing": {
        "types": [
            "Dress",
            "Blouse",
            "T-Shirt",
            "Jacket",
            "Jeans",
        ],
        "variants": [
            "Size S",
            "Size M",
            "Size L",
            "Size XL",
            "Free Size",
        ],
        "price_range": (100_000, 4_000_000),
    },

    "Shoes": {
        "types": [
            "Running Shoes",
            "Sneakers",
            "Casual Shoes",
            "Training Shoes",
            "Walking Shoes",
        ],
        "variants": [
            "Size 39",
            "Size 40",
            "Size 41",
            "Size 42",
            "Size 43",
        ],
        "price_range": (300_000, 5_000_000),
    },

    "Accessories": {
        "types": [
            "Backpack",
            "Wallet",
            "Belt",
            "Sunglasses",
            "Watch",
        ],
        "variants": [
            "Black",
            "Brown",
            "Blue",
            "Classic",
            "Premium",
        ],
        "price_range": (100_000, 5_000_000),
    },

    "Furniture": {
        "types": [
            "Office Chair",
            "Dining Table",
            "Bookshelf",
            "Coffee Table",
            "Storage Cabinet",
        ],
        "variants": [
            "Small",
            "Medium",
            "Large",
            "Wood",
            "Modern",
        ],
        "price_range": (500_000, 20_000_000),
    },

    "Kitchen": {
        "types": [
            "Cookware Set",
            "Frying Pan",
            "Kitchen Knife",
            "Electric Kettle",
            "Food Container Set",
        ],
        "variants": [
            "Small",
            "Medium",
            "Large",
            "Stainless Steel",
            "Premium",
        ],
        "price_range": (100_000, 8_000_000),
    },

    "Home Decor": {
        "types": [
            "Table Lamp",
            "Wall Clock",
            "Decorative Vase",
            "Picture Frame",
            "Floor Lamp",
        ],
        "variants": [
            "Small",
            "Medium",
            "Large",
            "Modern",
            "Classic",
        ],
        "price_range": (100_000, 5_000_000),
    },

    "Bedding": {
        "types": [
            "Bed Sheet Set",
            "Pillow",
            "Blanket",
            "Mattress Topper",
            "Duvet Cover",
        ],
        "variants": [
            "Single",
            "Double",
            "Queen",
            "King",
            "Premium",
        ],
        "price_range": (200_000, 8_000_000),
    },

    "Skincare": {
        "types": [
            "Facial Cleanser",
            "Moisturizer",
            "Serum",
            "Sunscreen",
            "Face Mask",
        ],
        "variants": [
            "50ml",
            "100ml",
            "150ml",
            "Sensitive Skin",
            "Hydrating",
        ],
        "price_range": (100_000, 3_000_000),
    },

    "Makeup": {
        "types": [
            "Lipstick",
            "Foundation",
            "Mascara",
            "Blush",
            "Eyeshadow",
        ],
        "variants": [
            "Natural",
            "Matte",
            "Glow",
            "Long Lasting",
            "Premium",
        ],
        "price_range": (100_000, 3_000_000),
    },

    "Hair Care": {
        "types": [
            "Shampoo",
            "Conditioner",
            "Hair Mask",
            "Hair Serum",
            "Hair Treatment",
        ],
        "variants": [
            "200ml",
            "300ml",
            "500ml",
            "Repair",
            "Moisturizing",
        ],
        "price_range": (100_000, 2_000_000),
    },

    "Fragrance": {
        "types": [
            "Eau de Parfum",
            "Eau de Toilette",
            "Body Mist",
            "Perfume",
            "Cologne",
        ],
        "variants": [
            "30ml",
            "50ml",
            "75ml",
            "100ml",
            "Fresh",
        ],
        "price_range": (300_000, 8_000_000),
    },

    "Fitness": {
        "types": [
            "Yoga Mat",
            "Dumbbell Set",
            "Resistance Band",
            "Exercise Ball",
            "Workout Bench",
        ],
        "variants": [
            "Light",
            "Medium",
            "Heavy",
            "Standard",
            "Pro",
        ],
        "price_range": (100_000, 8_000_000),
    },

    "Outdoor": {
        "types": [
            "Camping Tent",
            "Sleeping Bag",
            "Camping Chair",
            "Hiking Backpack",
            "Portable Table",
        ],
        "variants": [
            "Compact",
            "2 Person",
            "4 Person",
            "Large",
            "Premium",
        ],
        "price_range": (200_000, 10_000_000),
    },

    "Cycling": {
        "types": [
            "Cycling Helmet",
            "Bike Light",
            "Cycling Gloves",
            "Bike Pump",
            "Cycling Backpack",
        ],
        "variants": [
            "Small",
            "Medium",
            "Large",
            "Standard",
            "Pro",
        ],
        "price_range": (100_000, 5_000_000),
    },

    "Sportswear": {
        "types": [
            "Training Shirt",
            "Running Shorts",
            "Sports Jacket",
            "Training Pants",
            "Sports Bra",
        ],
        "variants": [
            "Size S",
            "Size M",
            "Size L",
            "Size XL",
            "Size XXL",
        ],
        "price_range": (150_000, 3_000_000),
    },
}


def generate_one_product(
    product_id: int,
    brands: list[dict],
    categories: list[dict],
    sellers: list[dict],
) -> dict:

    sub_categories = [
        category
        for category in categories
        if category["level"] == 2
    ]

    category = random.choice(sub_categories)
    brand = random.choice(brands)
    seller = random.choice(sellers)

    config = PRODUCT_CONFIG[category["category_name"]]

    product_type = random.choice(config["types"])
    variant = random.choice(config["variants"])

    product_name = (
        f"{brand['brand_name']} "
        f"{product_type} "
        f"{variant}"
    )

    min_price, max_price = config["price_range"]

    price = round(
        random.uniform(min_price, max_price),
        2,
    )

    sku = (
        f"{brand['brand_id']:02d}"
        f"{category['category_id']:02d}"
        f"{product_id:05d}"
    )

    start_created_at = max(
        brand["created_at"],
        category["created_at"],
        seller["created_at"],
        datetime(2024, 6, 1),
    )

    return {
        "product_id": product_id,
        "sku": sku,
        "product_name": product_name,
        "category_id": category["category_id"],
        "brand_id": brand["brand_id"],
        "seller_id": seller["seller_id"],
        "price": price,
        "stock_qty": random.randint(0, 500),
        "rating": round(random.uniform(3, 5), 1),
        "created_at": fake.date_time_between(
            start_date=start_created_at,
            end_date=datetime(2024, 12, 31),
        ),
        "is_active": random.choice([True, False]),
    }


def is_valid_product(
    product: dict,
    brands: list[dict],
    categories: list[dict],
    sellers: list[dict],
) -> bool:

    brand_ids = {
        brand["brand_id"]
        for brand in brands
    }

    category_ids = {
        category["category_id"]
        for category in categories
        if category["level"] == 2
    }

    seller_ids = {
        seller["seller_id"]
        for seller in sellers
    }

    return (
        len(product["sku"]) <= 20
        and len(product["product_name"]) <= 200
        and product["brand_id"] in brand_ids
        and product["category_id"] in category_ids
        and product["seller_id"] in seller_ids
        and product["price"] > 0
        and product["stock_qty"] >= 0
        and 0 <= product["rating"] <= 5
    )


def generate_products(
    brands: list[dict],
    categories: list[dict],
    sellers: list[dict],
    count: int = 3000,
) -> list[dict]:

    products = []
    product_id = 1

    while len(products) < count:
        product = generate_one_product(
            product_id=product_id,
            brands=brands,
            categories=categories,
            sellers=sellers,
        )

        if is_valid_product(
            product=product,
            brands=brands,
            categories=categories,
            sellers=sellers,
        ):
            products.append(product)
            product_id += 1

    return products