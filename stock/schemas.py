import strawberry
from typing import List
from resolvers import schema
from dao import (
    get_consumer_by_id, get_all_consumers, create_consumer, update_consumer, delete_consumer,
    get_supplier_by_id, get_all_suppliers, create_supplier, update_supplier, delete_supplier,
    get_product_by_id, get_all_products, create_product, update_product, delete_product,
    get_order_by_id, get_all_orders, create_order, update_order, delete_order
)


@strawberry.type
class Consumer:
    id: int
    name: str
    email: str

@strawberry.type
class Supplier:
    id: int
    name: str
    email: str

@strawberry.type
class Product:
    id: int
    name: str
    price: float

@strawberry.type
class Orders:
    id: int
    quantity: int
    consumer: Consumer
    supplier: Supplier
    product: Product
   

@strawberry.type
class Query:
    @strawberry.field
    def get_consumer(self, consumer_id: int) -> Consumer:
        return get_consumer_by_id(consumer_id)

    @strawberry.field
    def get_all_consumers(self) -> List[Consumer]:
        return get_all_consumers()

    @strawberry.field
    def get_supplier(self, supplier_id: int) -> Supplier:
        return get_supplier_by_id(supplier_id)

    @strawberry.field
    def get_all_suppliers(self) -> List[Supplier]:
        return get_all_suppliers()

    @strawberry.field
    def get_product(self, product_id: int) -> Product:
        return get_product_by_id(product_id)

    @strawberry.field
    def get_all_products(self) -> List[Product]:
        return get_all_products()

    @strawberry.field
    def get_order(self, order_id: int) -> Orders:
        return get_order_by_id(order_id)

    @strawberry.field
    def get_all_orders(self) -> List[Orders]:
        return get_all_orders()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_consumer(self, name: str, email: str) -> Consumer:
        return create_consumer(name, email)

    @strawberry.mutation
    def update_consumer(self, consumer_id: int, name: str, email: str) -> Consumer:
        return update_consumer(consumer_id, name, email)

    @strawberry.mutation
    def delete_consumer(self, consumer_id: int) -> Consumer:
        return delete_consumer(consumer_id)

    @strawberry.mutation
    def create_supplier(self, name: str, email: str) -> Supplier:
        return create_supplier(name, email)

    @strawberry.mutation
    def update_supplier(self, supplier_id: int, name: str, email: str) -> Supplier:
        return update_supplier(supplier_id, name, email)

    @strawberry.mutation
    def delete_supplier(self, supplier_id: int) -> Supplier:
        return delete_supplier(supplier_id)

    @strawberry.mutation
    def create_product(self, name: str, price: float, supplier_id: int) -> Product:
        return create_product(name, price, supplier_id)

    @strawberry.mutation
    def update_product(self, product_id: int, name: str, price: float, supplier_id: int) -> Product:
        return update_product(product_id, name, price, supplier_id)

    @strawberry.mutation
    def delete_product(self, product_id: int) -> Product:
        return delete_product(product_id)

    @strawberry.mutation
    def create_order(self, quantity: int, consumer_id: int, supplier_id:int, product_id: int) -> Orders:
        return create_order(quantity, consumer_id, supplier_id, product_id)

    @strawberry.mutation
    def update_order(self, order_id: int, quantity: int, consumer_id: int,supplier_id:int, product_id: int) -> Orders:
        return update_order(order_id, quantity, consumer_id, supplier_id,product_id)

    @strawberry.mutation
    def delete_order(self, order_id: int) -> Orders:
        return delete_order(order_id)


schema = strawberry.Schema(query=Query, mutation=Mutation)
