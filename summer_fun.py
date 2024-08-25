import re
from enum import Enum
from decimal import Decimal
from datetime import date


class Rating(Enum):
    FIRST_TIME = "First time"
    REGULAR = "Regular"
    SUPER_DUPER = "Super-duper"

    def __str__(self):
        return self.name


class Customer:
    def __init__(self, name: str, rating: Rating):
        if not isinstance(name, str):
            raise ValueError(f"Customer name must be a string.")
        if len(name) == 0:
            raise ValueError(f"Customer name must be non-empty.")
        if not isinstance(rating, Rating):
            raise ValueError(f"Customer rating must be of type Rating, but is of type {type(rating)}.")

        self.name = name
        self.rating = rating

    def __str__(self):
        return f"{self.name} ({self.rating})"


class Product:
    _EAN_PATTERN = re.compile(r"^\d{13}$")

    def __init__(self, ean: str, name: str, description: str, base_price: Decimal, base_discount=Decimal(0)):
        if not Product._EAN_PATTERN.match(ean):
            raise ValueError(f"Given ean {ean} is not valid. An ean has exactly 13 digits.")
        if not isinstance(name, str):
            raise ValueError(f"Product name must be a string.")
        if len(name) == 0:
            raise ValueError(f"Product name must be non-empty.")
        if not (isinstance(description, str) or description is None):
            raise ValueError(f"Product description must be a string or None, but is '{description}'")
        if not isinstance(base_price, Decimal):
            raise ValueError(f"Product base price must be of type Decimal.")
        if not base_price >= 0:
            raise ValueError(f"Product base price must be greater or equal to zero.")
        if not isinstance(base_discount, Decimal):
            raise ValueError(f"Product discount must be of type Decimal.")
        if base_discount < 0 or base_discount > 1:
            raise ValueError(f"Product discount must be between 0 and 1.")

        self.ean = ean
        self.name = name
        self.description = description
        self.base_price = base_price
        self.base_discount = base_discount

    def calculate_price_for_customer(self, customer: Customer, date_of_purchase: date) -> Decimal:
        return Decimal(0)
