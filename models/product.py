from dataclasses import dataclass
from typing import List

from models.dimension import Dimension
from models.meta import Meta
from models.review import Review


@dataclass
class Product:
    id: int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: float
    rating: float
    stock: int
    tags: List[str]
    sku: str
    weight: int
    dimensions: Dimension
    warrantyInformation: str
    shippingInformation: str
    availabilityStatus: str
    reviews: List[Review]
    returnPolicy: str
    minimumOrderQuantity: int
    meta: Meta
    images: List[str]
    thumbnail: str
    brand = "Unknow"