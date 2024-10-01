from datetime import datetime
from uuid import uuid4

from data.init import curs
from dto.product import CreateProduct
from model.product import Product

assert curs is not None

init_table_sql = """
CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    created_at TEXT NOT NULL,
    created_by TEXT NOT NULL
);
"""

curs.execute(init_table_sql)

def row_to_product(row: tuple) -> Product:
    return Product(id=row[0], name=row[1], description=row[2], price=row[3], created_at=row[4], created_by=row[5])

def create_product(product_data: CreateProduct, created_by: str) -> Product:
    id = str(uuid4())
    name = product_data.name
    description = product_data.description
    price = product_data.price
    created_at = datetime.now()

    sql = """
    INSERT INTO products (id, name, description, price, created_at, created_by) values (:id, :name, :description, :price, :created_at, :created_by)
    """
    params = {
        "id": id,
        "name": name,
        "description": description,
        "price": price,
        "created_at": created_at,
        "created_by": created_by
    }
    curs.execute(sql, params)

    return Product(id=id, name=name, description=description, price=price, created_at=created_at, created_by=created_by)

def get_product_by_id(id: str) -> Product | None:
    sql = "SELECT * FROM products WHERE id = :id"
    params = {"id": id}
    row = curs.execute(sql, params).fetchone()

    return row_to_product(row) if row else None

def get_product_by_name(name: str) -> Product | None:
    sql = "SELECT * FROM products WHERE name = :name"
    params = {"name": name}
    row = curs.execute(sql, params).fetchone()

    return row_to_product(row) if row else None

def get_products() -> list[Product]:
    sql = "SELECT * FROM products"
    rows = curs.execute(sql).fetchall()

    return [row_to_product(row) for row in rows]
