import pytest
from products.models import Product

@pytest.mark.django_db
def test_create_product():
    print("Создаю товар")
    product = Product.objects.create(
        name='Test Product',
        description='Test Description',
        price=10.00
    )
    assert product.pk is not None
    assert product.name == 'Test Product'

@pytest.mark.django_db
def test_update_product():
    print("Редактирую товар")
    product = Product.objects.create(
        name='Test Product',
        description='Test Description',
        price=10.00
    )
    product.name = 'Updated Product'
    product.save()
    assert product.name == 'Updated Product'

@pytest.mark.django_db
def test_delete_product():
    print("удаляю товар")
    product = Product.objects.create(
        name='Test Product',
        description='Test Description',
        price=10.00
    )
    pk = product.pk
    product.delete()
    assert not Product.objects.filter(pk=pk).exists()