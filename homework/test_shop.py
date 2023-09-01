"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 2000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity

        assert product.check_quantity(product.quantity)
        assert product.check_quantity(product.quantity + 1)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        items = 10
        all_quantity = product.quantity
        product.buy(items)

        assert product.quantity == all_quantity - items

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        buying_quantity = product.quantity + 1
        with pytest.raises(ValueError) as exception:
            product.buy(buying_quantity)
        assert exception.typename == 'ValueError'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_cart(self, cart, product):
        cart.add_product(product, 200)
        assert cart.products[product] == 200

        # add same product
        cart.add_product(product, 500)
        assert cart.products[product] == 700

    def test_remove_product_from_cart(self, cart, product):
        cart.add_product(product, 100)
        cart.remove_product(product, 150)
        assert product not in cart.products

        cart.add_product(product, 100)
        cart.remove_product(product)
        assert cart not in cart.products

        cart.add_product(product, 100)
        cart.remove_product(product, 50)
        assert cart.products[product] == 50

    def test_clear_product_cart(self, cart, product):
        cart.add_product(product, 150)
        cart.clear()
        assert len(cart.products) == 0

    def test_total_price_of_products_in_cart(self, cart, product):
        cart.add_product(product, 120)
        cart.get_total_price()
        assert (product.price * 120) == cart.get_total_price()

    def test_buy_cart(self, cart, product):
        cart.add_product(product, 225)
        cart.buy()
        assert product.quantity == 1775
