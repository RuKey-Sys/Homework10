from celery import shared_task
from .models import Product
from myshop.celery import app

@shared_task
def add_new_product_to_db(product_name, product_price, product_description):
    print(f'Добавляем новый товар: {product_name}')
    
    product = Product(
        name=product_name,
        price=product_price,
        description=product_description
    )
    
    print(f'Товар {product_name} добавлен в базу данных')