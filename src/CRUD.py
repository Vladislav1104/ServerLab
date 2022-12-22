from sqlalchemy.orm import Session

from src import models, schemas

def create_provider(db: Session, provider: schemas.providerCreate):

    db_provider = models.Provider(**provider.dict())
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider


def create_flower(db: Session, flower: schemas.flowerCreate, provider_id: int):

    db_flower = models.Flower(**flower.dict(), provider_id = provider_id)
    db.add(db_flower)
    db.commit()
    db.refresh(db_flower)
    return db_flower

def create_customer(db: Session, customer: schemas.customerCreate):

    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer    

def create_contract(db: Session, contract: schemas.contractCreate, customers_id: int):

    db_contract = models.Contract(**contract.dict(), customers_id = customers_id)
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

def create_order(db: Session, order: schemas.orderCreate, contract_id : int, flower_id : int):

    db_order = models.Order(**order.dict(), contract_id = contract_id, flower_id = flower_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_provider_by_id(db: Session, provider_id: int):

    return db.query(models.Provider).filter(models.Provider.id == provider_id).first()

def get_flower_by_id(db: Session, flower_id: int):

    return db.query(models.Flower).filter(models.Flower.id == flower_id).first()

def get_customer_by_id(db: Session, customer_id: int):
 
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def get_contract_by_id(db: Session, contract_id: int):
    return db.query(models.Contract).filter(models.Contract.id == contract_id).first()

def get_order_by_id(db: Session, order_id: int):
 
    return db.query(models.Order).filter(models.Order.id == order_id).first()



def get_provider_by_name(db: Session, name: str):
    return db.query(models.Provider).filter(models.Provider.name == name).first()

def get_flower_by_flowerName(db: Session, flowerName: str):
    return db.query(models.Flower).filter(models.Flower.flowerName == flowerName).first()

def get_customer_by_name(db: Session, name: str):
    return db.query(models.Customer).filter(models.Customer.name == name).first()

def get_contract_by_date_of_conf(db: Session, date_of_conf: str):
    return db.query(models.Contract).filter(models.Contract.date_of_conf == date_of_conf).first()

def get_order_by_seedlings(db: Session, seedlings: int):
    return db.query(models.Order).filter(models.Order.seedlings == seedlings).first()    


def get_provider(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Provider).offset(skip).limit(limit).all()

def get_flower(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Flower).offset(skip).limit(limit).all()

def get_customer(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Customer).offset(skip).limit(limit).all()

def get_contract(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Contract).offset(skip).limit(limit).all()
    
def get_order(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Order).offset(skip).limit(limit).all()