-- 1. BRAND
CREATE TABLE brand (
    brand_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(100) UNIQUE NOT NULL,
    country VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL
);

-- 2. CATEGORY
CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL,
    parent_category_id INT,
    level SMALLINT NOT NULL,
    created_at TIMESTAMP NOT NULL,

    CONSTRAINT fk_category_parent
        FOREIGN KEY (parent_category_id)
        REFERENCES category(category_id),

    CONSTRAINT chk_category_level
        CHECK (level IN (1, 2)),

    CONSTRAINT chk_category_hierarchy
        CHECK (
            (level = 1 AND parent_category_id IS NULL)
            OR
            (level = 2 AND parent_category_id IS NOT NULL)
        )
);

-- 3. SELLER
CREATE TABLE seller (
    seller_id SERIAL PRIMARY KEY,
    seller_code VARCHAR(30) UNIQUE NOT NULL,
    seller_name VARCHAR(150) NOT NULL,
    join_date DATE NOT NULL,
    seller_type VARCHAR(50) NOT NULL,
    rating NUMERIC(2,1) NOT NULL,
    country VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL,

    CONSTRAINT chk_seller_type
        CHECK (seller_type IN ('Official', 'Marketplace')),

    CONSTRAINT chk_seller_rating
        CHECK (rating >= 0 AND rating <= 5),

    CONSTRAINT chk_seller_created_at
        CHECK (created_at::date >= join_date)
);


-- 4. CUSTOMER
CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL,

    CONSTRAINT chk_customer_gender
        CHECK (gender IN ('Male', 'Female'))
);


-- 5. PROMOTION
CREATE TABLE promotion (
    promotion_id SERIAL PRIMARY KEY,
    promotion_code VARCHAR(30) UNIQUE NOT NULL,
    promotion_name VARCHAR(100) NOT NULL,
    promotion_type VARCHAR(50) NOT NULL,
    discount_type VARCHAR(20) NOT NULL,
    discount_value NUMERIC(10,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP NOT NULL,

    CONSTRAINT chk_promotion_type
        CHECK (
            promotion_type IN (
                'product',
                'category',
                'seller',
                'flash_sale'
            )
        ),

    CONSTRAINT chk_discount_type
        CHECK (
            discount_type IN (
                'percentage',
                'fixed_amount'
            )
        ),

    CONSTRAINT chk_discount_value
        CHECK (
            discount_value > 0
            AND (
                discount_type = 'fixed_amount'
                OR discount_value <= 100
            )
        ),

    CONSTRAINT chk_promotion_start
        CHECK (start_date >= created_at::date),

    CONSTRAINT chk_promotion_end
        CHECK (end_date >= start_date)
);


-- 6. PRODUCT
CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    sku VARCHAR(20) UNIQUE NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    category_id INT NOT NULL,
    brand_id INT NOT NULL,
    seller_id INT NOT NULL,
    price NUMERIC(12,2) NOT NULL,
    stock_qty INT NOT NULL,
    rating NUMERIC(2,1) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_product_category
        FOREIGN KEY (category_id)
        REFERENCES category(category_id),

    CONSTRAINT fk_product_brand
        FOREIGN KEY (brand_id)
        REFERENCES brand(brand_id),

    CONSTRAINT fk_product_seller
        FOREIGN KEY (seller_id)
        REFERENCES seller(seller_id),

    CONSTRAINT chk_product_price
        CHECK (price > 0),

    CONSTRAINT chk_product_stock
        CHECK (stock_qty >= 0),

    CONSTRAINT chk_product_rating
        CHECK (rating >= 0 AND rating <= 5)
);


-- 7. PROMOTION_PRODUCT
CREATE TABLE promotion_product (
    promo_product_id SERIAL PRIMARY KEY,
    promotion_id INT NOT NULL,
    product_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL,

    CONSTRAINT fk_promotion_product_promotion
        FOREIGN KEY (promotion_id)
        REFERENCES promotion(promotion_id),

    CONSTRAINT fk_promotion_product_product
        FOREIGN KEY (product_id)
        REFERENCES product(product_id),

    CONSTRAINT uq_promotion_product
        UNIQUE (promotion_id, product_id)
);

COMMIT;