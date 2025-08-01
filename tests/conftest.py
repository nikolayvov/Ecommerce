import pytest

from src.main_14_1 import Product, Category


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product4():
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def category1(product1, product2):
    Category.category_count = 0
    Category.product_count = 0
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения"
                    "дополнительных функций для удобства жизни",
                    [product1, product2])


@pytest.fixture
def category2(product4):
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом"
                    " и помощником",
                    [product4])


@pytest.fixture
def empty_category():
    Category.category_count = 0
    Category.product_count = 0
    return Category("Empty Category", "Категория без продуктов", [])
