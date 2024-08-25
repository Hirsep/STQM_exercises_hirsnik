import pytest
from datetime import date
from decimal import Decimal
from summer_fun import Customer, Product, Rating


# First time customer, valid date, no base discount
def test_tc1():
    product = Product("123", "Product A", "Description", Decimal("111"))
    customer = Customer("First Timer", Rating.FIRST_TIME)
    result = product.calculate_price_for_customer(customer, date(2024, 7, 2))
    assert result == Decimal("105.45")


def test_tc2():
    product = Product("123", "Product A", "Description", Decimal("111"))
    customer = Customer("First Timer", Rating.FIRST_TIME)
    result = product.calculate_price_for_customer(customer, date(2024, 7, 1))
    assert result == Decimal("105.45")


def test_tc3():
    product = Product("123", "Product A", "Description", Decimal("111"))
    customer = Customer("First Timer", Rating.FIRST_TIME)
    result = product.calculate_price_for_customer(customer, date(2024, 8, 29))
    assert result == Decimal("105.45")


# First time customer, valid date, base discount applied
def test_tc4():
    product = Product("123", "Product A", "Description", Decimal("111"), Decimal("0.1"))
    customer = Customer("First Timer", Rating.FIRST_TIME)
    result = product.calculate_price_for_customer(customer, date(2024, 7, 2))
    assert result == Decimal("94.91")


# First time customer, weekend, no base discount
def test_tc5():
    product = Product("123", "Product A", "Description", Decimal("111"))
    customer = Customer("First Timer", Rating.FIRST_TIME)
    result = product.calculate_price_for_customer(customer, date(2024, 7, 5))  # Friday (Weekend)
    assert result == Decimal("99.9")


# First time customer, weekend, base discount applied
def test_tc6():
    product = Product("123", "Product A", "Description", Decimal("111"), Decimal("0.1"))
    customer = Customer("First Timer", Rating.FIRST_TIME)
    result = product.calculate_price_for_customer(customer, date(2024, 7, 5))  # Friday (Weekend)
    assert result == Decimal("89.91")


# Regular customer, valid date, no base discount
def test_tc7():
    product = Product("123", "Product A", "Description", Decimal("111"))
    customer = Customer("Regular Customer", Rating.REGULAR)
    result = product.calculate_price_for_customer(customer, date(2024, 7, 22))
    assert result == Decimal("99.9")


# Regular customer, weekend, base discount applied
def test_tc8():
    product = Product("123", "Product A", "Description", Decimal("111"), Decimal("0.1"))
    customer = Customer("Regular Customer", Rating.REGULAR)
    result = product.calculate_price_for_customer(customer, date(2024, 8, 16))  # Friday
    assert result == Decimal("79.92")


# Super duper customer, valid date, no base discount
def test_tc9():
    product = Product("123", "Product A", "Description", Decimal("111"))
    customer = Customer("Super Duper Customer", Rating.SUPER_DUPER)
    result = product.calculate_price_for_customer(customer, date(2024, 7, 22))
    assert result == Decimal("94.35")


# Super duper customer, weekend, base discount applied
def test_tc10():
    product = Product("123", "Product A", "Description", Decimal("111"), Decimal("0.15"))
    customer = Customer("Super Duper Customer", Rating.SUPER_DUPER)
    result = product.calculate_price_for_customer(customer, date(2024, 8, 16))  # Friday
    assert result == Decimal("66.05")


# Sale period boundary cases
def test_tc11():
    product = Product("123", "Product A", "Description", Decimal("111"))
    customer = Customer("Regular Customer", Rating.REGULAR)
    result = product.calculate_price_for_customer(customer, date(2024, 6, 30))
    assert result == Decimal("111")  # No discounts


def test_tc12():
    product = Product("123", "Product A", "Description", Decimal("111"))
    customer = Customer("Regular Customer", Rating.REGULAR)
    result = product.calculate_price_for_customer(customer, date(2024, 9, 1))
    assert result == Decimal("111")  # No discounts


# Invalid cases for date, customer type, product price
def test_tc13_invalid_date():
    product = Product("123", "Product A", "Description", Decimal("111"))
    customer = Customer("Regular Customer", Rating.REGULAR)
    with pytest.raises(ValueError):
        product.calculate_price_for_customer(customer, "ABC")  # Invalid date


def test_tc14_invalid_customer_type():
    product = Product("123", "Product A", "Description", Decimal("111"))
    with pytest.raises(ValueError):
        product.calculate_price_for_customer("NOT_VALID", date(2024, 7, 22))  # Invalid customer


def test_tc15_invalid_price():
    with pytest.raises(ValueError):
        product = Product("123", "Product A", "Description", Decimal("-111"))  # Invalid price


def test_tc16_invalid_price_format():
    with pytest.raises(ValueError):
        product = Product("123", "Product A", "Description", "ABC")  # Invalid price format


def test_tc17_invalid_base_discount():
    with pytest.raises(ValueError):
        product = Product("123", "Product A", "Description", Decimal("111"), Decimal("1.1"))  # Invalid base discount