from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import CRUD, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():   # pragma: no cover
    """
    Задаем зависимость к БД. При каждом запросе будет создаваться новое
    подключение.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()   

@app.get("/providers/", response_model=list[schemas.provider])
def get_provider(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    provider = CRUD.get_provider(db, skip=skip, limit=limit)
    return provider

@app.get("/providers/{provider_id}", response_model=schemas.provider)
def get_provider_by_id(provider_id: int, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_provider = CRUD.get_provider_by_id(db, provider_id = provider_id)
    if db_provider is None:
        raise HTTPException(status_code=400, detail="Provider not found")
    return db_provider

@app.post("/providers/", response_model=schemas.provider)
def create_provider(provider: schemas.providerCreate, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_provider = CRUD.get_provider_by_name(db, name = provider.name)
    if db_provider:
        raise HTTPException(status_code=400, detail="Provider already registered")
    return CRUD.create_provider(db=db, provider=provider)

@app.get("/flowers/", response_model=list[schemas.flower])
def get_flower(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    flower = CRUD.get_flower(db, skip=skip, limit=limit)
    return flower

@app.get("/flowers/{flower_id}", response_model=schemas.flower)
def get_flower_by_id(flower_id: int, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_flower = CRUD.get_flower_by_id(db, flower_id = flower_id)
    if db_flower is None:
        raise HTTPException(status_code=400, detail="Flower not found")
    return db_flower

@app.post("/flowers/{provider_id}/providers", response_model=schemas.flower)
def create_flower(provider_id: int, flower: schemas.flowerCreate, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_flower = CRUD.get_flower_by_flowerName(db, flowerName = flower.flowerName)
    if db_flower:
        raise HTTPException(status_code=400, detail="Flower already registered")
    return CRUD.create_flower(db=db, provider_id = provider_id, flower = flower)

@app.get("/customers/", response_model=list[schemas.customer])
def get_customer(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    customer = CRUD.get_customer(db, skip=skip, limit=limit)
    return customer

@app.get("/customers/{customer_id}", response_model=schemas.customer)
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_customer = CRUD.get_customer_by_id(db, customer_id = customer_id)
    if db_customer is None:
        raise HTTPException(status_code=400, detail="Customer not found")
    return db_customer

@app.post("/customers/", response_model=schemas.customer)
def create_customer(customer: schemas.customerCreate, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_customer = CRUD.get_customer_by_name(db, name = customer.name)
    if db_customer:
        raise HTTPException(status_code=400, detail="Customer already registered")
    return CRUD.create_customer(db=db, customer = customer)

@app.get("/contracts/", response_model=list[schemas.contract])
def get_contract(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    contract = CRUD.get_contract(db, skip=skip, limit=limit)
    return contract

@app.get("/contracts/{contract_id}", response_model=schemas.contract)
def get_contract_by_id(contract_id: int, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_contract = CRUD.get_contract_by_id(db, contract_id = contract_id)
    if db_contract is None:
        raise HTTPException(status_code=400, detail="Contract not found")
    return db_contract

@app.post("/contracts/{customers_id}/customers/", response_model=schemas.contract)
def create_contract(customers_id : int, contract: schemas.contractCreate, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_contract = CRUD.get_contract_by_date_of_conf(db, date_of_conf = contract.date_of_conf)
    if db_contract:
        raise HTTPException(status_code=400, detail="Contract already registered")
    return CRUD.create_contract(db=db, contract = contract, customers_id = customers_id)

@app.get("/orders/", response_model=list[schemas.order])
def get_order(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    order = CRUD.get_order(db, skip=skip, limit=limit)
    return order

@app.get("/orders/{order_id}", response_model=schemas.order)
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_order = CRUD.get_order_by_id(db, order_id = order_id)
    if db_order is None:
        raise HTTPException(status_code=400, detail="Order not found")
    return db_order

@app.post("/orders/{contract_id}/flower/{flower_id}/contracts/", response_model=schemas.order)
def create_order(contract_id : int, flower_id : int, order: schemas.orderCreate, db: Session = Depends(get_db)):
    """
    alembic.ini
    """
    db_order = CRUD.get_order_by_seedlings(db, seedlings = order.seedlings)
    if db_order:
        raise HTTPException(status_code=400, detail="Order already registered")
    return CRUD.create_order(db=db, order = order, contract_id = contract_id, flower_id = flower_id)