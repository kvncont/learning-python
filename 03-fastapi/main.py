""" FastAPI CRUD API """

import uuid
from decimal import Decimal
from typing import ClassVar

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import UUID4, BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class Product(BaseModel):
    """Product model"""

    product_schema: ClassVar = {
        "properties": {
            "id": {"description": "Product ID generated by UUID4"},
            "name": {"description": "Product name"},
            "description": {"description": "Product description"},
            "brand": {"description": "Product brand"},
            "price": {"description": "Product price"},
            "available": {"description": "Product availability"},
        },
        "example": {
            "id": uuid.uuid4(),
            "name": "Rice",
            "description": "Rice 100% grain purity",
            "brand": "Indiana",
            "price": 6.55,
            "available": True,
        },
    }

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="forbid",
        json_schema_extra=product_schema,
    )

    id: UUID4 =  
    name: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=250)
    brand: str = Field(min_length=2, max_length=30)
    price: Decimal = Field(ge=0.0)
    available: bool = Field(default=True)


info = {
    "title": "Products API",
    "description": "API de prueba usando FastAPI",
    "contact": {"name": "Kevin Contreras", "email": "kvncont@gmail.com"},
    "version": "0.1.0",
}

app = FastAPI(**info)

db: list[Product] = []


@app.get("/products/", status_code=status.HTTP_200_OK)
def get_products() -> list[Product]:
    """
    # Get all products

    ## Returns:
    - **list[Product]**: List of products

    """
    return db


@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
def get_product_by_id(product_id: UUID4) -> Product:
    """
    # Get product by ID

    ## Args:
    - **id (UUID4)**: Product ID

    ## Returns:
    - **Product**: Product object
    """
    for product in db:
        if product.id == product_id:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
    )


@app.put("/products/", status_code=status.HTTP_200_OK)
def upsert_product(new_product: Product, response: Response) -> Product:
    """
    # Upsert a product

    ## Args:
    - **upsert_product (Product)**: Product object
    - **response (Response)**: FastAPI response object

    ## Returns:
    - **Product**: Product object
    """
    for index, product in enumerate(db):
        if product.id == new_product.id:
            db[index] = new_product
            return new_product
    response.status_code = status.HTTP_201_CREATED
    db.append(new_product)
    return new_product


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_by_id(product_id: UUID4) -> None:
    """
    # Delete product by ID

    ## Args:
    - **id (UUID4)**: Product ID

    ## Returns:
    - **None**
    """
    for index, product in enumerate(db):
        if product.id == product_id:
            db.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
    )
