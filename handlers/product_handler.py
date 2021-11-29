from sqlalchemy import select, delete, update
from models.product import Product
from handlers import Session


def adding_product(add_product):
    """Starts session to add product and automatically ends it"""
    with Session.begin() as session:
        session.add(add_product)
        session.commit()

def all_products():
    """Starts session to show all products and automatically ends it"""
    with Session.begin() as session:
        statement = select(Product.serial, Product.description, Product.price)
        result = session.execute(statement).all()
        for row in result:
            print(row)

def removing_product(delete_product: str = None):
    """Starts session to remove product and automatically ends it"""
    with Session.begin() as session:
        stmt = delete(Product).where(Product.description == delete_product).\
                execution_options(synchronize_session='fetch')
        session.execute(stmt)

def show_product(search_product):
    """Starts session to show a product and automatically ends it"""
    with Session.begin() as session:
        stmt = select(Product.description).filter_by(description=search_product)
        result = session.execute(stmt).all()
        print(result)

def get_product(product):
    """Starts session to show a product and automatically ends it"""
    with Session.begin() as session:
        stmt = select(Product.serial, Product.description, Product.price).filter_by(description=product)
        result = session.execute(stmt).all()
    return result
        

