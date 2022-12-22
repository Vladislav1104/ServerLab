from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению

def test_create_provider():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/providers/",
        json={"provider_code": "1", "name" : "greenWorld", "adress": "ulica chego-to"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["provider_code"] == 1

def test_create_exist_provider():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/providers/",
        json={"provider_code": "1", "name" : "greenWorld", "adress": "ulica chego-to"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Provider already registered"

def test_get_provider():
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/providers/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["provider_code"] == 1

def test_get_provider_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/providers/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["provider_code"] == 1

def test_provider_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/providers/2")
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Provider not found"

def test_create_customer():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/customers/",
        json={"customer_code" : "1", "name" : "greenLand", "adress" : "chto-to gde-to", "phone_number" : "89234728911"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["customer_code"] == 1

def test_create_exist_customer():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/customers/",
        json={"customer_code" : "1", "name" : "greenLand", "adress" : "chto-to gde-to", "phone_number" : "89234728911"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Customer already registered"

def test_get_customer():
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/customers/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["customer_code"] == 1

def test_get_customer_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/customers/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["customer_code"] == 1

def test_customer_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/customers/2")
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Customer not found"

def test_flower():
    """
    Тест на добавление Item пользователю
    """
    response = client.post(
        "/flowers/1/providers/",
        json={"flower_code" : "1", "flowerName" : "geocind", "price" : "100", "provider_id" : "greenWorld.id"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["flower_code"] == 1
    assert data["flowerName"] == "geocind"
    assert data["price"] == 100
    assert data["provider_id"] == 1

def test_create_exist_flower():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/flowers/1/providers/",
        json={"flower_code" : "1", "flowerName" : "geocind", "price" : "100", "provider_id" : "greenWorld.id"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Flower already registered"

def test_get_flower():
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/flowers/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["flower_code"] == 1

def test_get_flower_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/flowers/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["flower_code"] == 1

def test_flower_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/flowers/2")
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Flower not found"

def test_add_contract_to_providers():
    """
    Тест на добавление Item пользователю
    """
    response = client.post(
        "/contracts/1/customers/",
        json={"contract_code" : "1", "date_of_conf" : "2001,9,9", "date_of_exec" : "2001,9,12", "customers_id" : 1}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["contract_code"] == 1
    assert data["date_of_conf"] == "2001,9,9"
    assert data["date_of_exec"] == "2001,9,12"
    assert data["customers_id"] == 1

def test_create_exist_contract():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/contracts/1/customers/",
        json={"contract_code" : "1", "date_of_conf" : "2001,9,9", "date_of_exec" : "2001,9,12", "customers_id" : 1}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Contract already registered"

def test_get_contract():
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/contracts/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["contract_code"] == 1

def test_get_contract_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/contracts/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["contract_code"] == 1

def test_contract_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/contracts/2")
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Contract not found"

def test_add_order():
    """
    Тест на добавление Item пользователю
    """
    response = client.post(
        "/orders/1/flower/1/contracts/",
        json={"seedlings" : 10000, "contract_id" : 1, "flower_id" : 1}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["seedlings"] == 10000
    assert data["contract_id"] == 1
    assert data["flower_id"] == 1

def test_create_exist_order():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/orders/1/flower/1/contracts/",
        json={"seedlings" : 10000, "contract_id" : 1, "flower_id" : 1}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Order already registered"

def test_get_order():
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/orders/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["seedlings"] == 10000

def test_get_order_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/orders/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["seedlings"] == 10000

def test_order_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/orders/2")
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Order not found"

