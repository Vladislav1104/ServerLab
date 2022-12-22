from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):    # pragma: no cover
        return f"<{type(self).__name__}(id={self.id})>"


class Provider(BaseModel):
    """
    Таблица поставщиков
    """
    __tablename__ = "providers"

    provider_code = Column(Integer)
    name = Column(String)
    adress = Column(String)

    flower = relationship("Flower", back_populates="provider")

class Flower(BaseModel):
    """
    Таблица цветов
    """    
    __tablename__ = "flowers"

    flower_code = Column(Integer)
    flowerName = Column(String)
    price = Column(Integer)

    provider_id = Column(Integer, ForeignKey("providers.id"))
    provider = relationship("Provider", back_populates = "flower")
    order = relationship("Order", back_populates = "flower")

class Customer(BaseModel):
    """
    Таблица заказчиков
    """
    __tablename__ = "customers"

    customer_code = Column(Integer)
    name = Column(String)
    adress = Column(String)
    phone_number = Column(Integer)
    
    contract = relationship("Contract", back_populates = "customer")

class Contract(BaseModel):
    """
    Таблица договоров
    """
    __tablename__ = "contracts"
     
    contract_code = Column(Integer)
    date_of_conf = Column(String)
    date_of_exec = Column(String)

    customers_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates = "contract")
    order = relationship("Order", back_populates  = "contract")

class Order (BaseModel):
    """
    Таблица заказов
    """
    __tablename__ = "orders"

    seedlings = Column(Integer)

    contract_id = Column(Integer, ForeignKey("contracts.id"))
    contract = relationship("Contract", back_populates = "order")
    flower_id = Column(Integer, ForeignKey("flowers.id"))
    flower = relationship("Flower", back_populates = "order")