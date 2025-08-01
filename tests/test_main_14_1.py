from src.main_14_1 import Category


def test_product_1(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product_2(product2):
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8


def test_product_types(product1):
    assert isinstance(product1.name, str)
    assert isinstance(product1.description, str)
    assert isinstance(product1.price, float)
    assert isinstance(product1.quantity, int)


def test_products_distinct(product1, product2):
    assert product1 != product2
    assert product1.name != product2.name


def test_category1(category1, product1, product2):
    assert category1.name == "Смартфоны"
    assert len(category1.products) == 2
    assert category1.products == [product1, product2]


def test_category2(category2, product4):
    assert category2.name == "Телевизоры"
    assert category2.description.startswith("Современный телевизор")
    assert len(category2.products) == 1
    assert category2.products == [product4]


def test_category_attributes_types(category1):
    assert isinstance(category1.name, str)
    assert isinstance(category1.description, str)
    assert isinstance(category1.products, list)


def test_counters(category1, category2):
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_counters_no_products():
    Category.category_count = 0
    Category.product_count = 0


def test_empty_category_counts(empty_category):
    assert empty_category.name == "Empty Category"
    assert empty_category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0
