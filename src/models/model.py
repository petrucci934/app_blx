from pydantic import BaseModel
from typing import Optional,List


class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: int
    my_products: List[Product]
    my_sales: List[Order]
    my_orders: List[Order]


class Product(BaseModel):
    id: Optional[str] = None
    user: User
    name: str
    detail: str
    price: float
    available: bool = False

class Order(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    amount: int
    delivery: bool = False
    address: str
    observations: Optional[str] = "Sem observações"


