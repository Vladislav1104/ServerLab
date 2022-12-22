from pydantic import BaseModel

class orderBase (BaseModel) : 
    """
    alembic.ini
    """
    seedlings : int

class orderCreate (orderBase) :
    """
    alembic.ini
    """
    pass

class order (orderBase) :
    """
    alembic.ini
    """

    id : int
    contract_id : int
    flower_id : int

    class Config :
        """
        """
        orm_mode = True     

class flowerBase (BaseModel) : 
    """
    Базовый класс для Видов цветов
    """
    flower_code : int
    flowerName : str
    price : int

class flowerCreate (flowerBase) :
    """
    Класс для создания Видов цветов, наследуется от providerBase, но не содержит наполнительных полей
    """
    pass

class flower (flowerBase) :
    """
    Класс для отображения flower, наследуются от базового flowerBase поля значений будем получаать из БД
    """

    id : int
    provider_id : int
    orders : list[order] = []

    class Config :
        """
        Задание настройки для возможности работать с объектами ORM 
        """
        orm_mode = True

class providerBase (BaseModel) : 
    """
    Базовый класс для Поставщиков
    """
    provider_code : int
    name : str
    adress : str

class providerCreate (providerBase) :
    """
    Класс для создания Поставщиков, наследуется от providerBase, но не содержит наполнительных полей
    """
    pass

class provider (providerBase) :
    """
    Класс для отображения provider, наследуются от базового providerBase поля значений будем получаать из БД
    """

    id : int
    flowers: list[flower] = []

    class Config :
        """
        Задание настройки для возможности работать с объектами ORM 
        """
        orm_mode = True

class contractBase (BaseModel) : 
    """
    alembic.ini
    """
    contract_code : int
    date_of_conf : str
    date_of_exec : str

class contractCreate (contractBase) :
    """
    alembic.ini
    """
    pass

class contract (contractBase) :
    """
    alembic.ini
    """

    id : int
    customers_id : int
    orders : list[order] = []

    class Config :
        """
        """
        orm_mode = True

class customerBase (BaseModel) : 
    """
    alembic.ini
    """
    customer_code : int
    name : str
    adress : str
    phone_number : int

class customerCreate (customerBase) :
    """
    alembic.ini
    """
    pass

class customer (customerBase) :
    """
    alembic.ini
    """

    id : int
    contracts : list[contract] = []
    
    

    class Config :
        """
        """
        orm_mode = True