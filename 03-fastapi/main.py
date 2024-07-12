import uuid
from pydantic import UUID4, BaseModel, Field
from fastapi import FastAPI, HTTPException, Response, status


class Product(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4,
                      description="Product ID", example=uuid.uuid4())
    name: str = Field(description="Product Name",
                      example="Rice", min_length=2, max_length=100)
    description: str = Field(description="Product Description",
                             example="This is a rice", min_length=2, max_length=250)
    brand: str = Field(description="Product Brand",
                       example="Indiana", min_length=2, max_length=30)
    price: float = Field(description="Product Price", example=100.0, ge=0.0)
    available: bool = Field(
        default=True, description="Product Availability", example=True)


info = {
    "title": "Products API",
    "description": "API de prueba usando FastAPI",
    "contact": {
        "name": "Kevin Contreras",
        "email": "kvncont@gmail.com"
    },
    "version": "0.1.0"
}

app = FastAPI(**info)

products: list[Product] = []


@app.get("/products/", status_code=status.HTTP_200_OK)
def get_products() -> list[Product]:
    return products


@app.get("/products/{id}", status_code=status.HTTP_200_OK)
def get_product_by_id(id: UUID4) -> Product:
    for product in products:
        if product.id == id:
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Product not found")


@app.put("/products/", status_code=status.HTTP_200_OK)
def upsert_product(upsert_product: Product, response: Response) -> Product:
    for index, product in enumerate(products):
        if product.id == upsert_product.id:
            products[index] = upsert_product
            return upsert_product
    response.status_code = status.HTTP_201_CREATED
    products.append(upsert_product)
    return upsert_product


@app.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_by_id(id: UUID4) -> None:
    for index, product in enumerate(products):
        if product.id == id:
            products.pop(index)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Product not found")

