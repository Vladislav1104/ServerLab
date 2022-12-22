"""empty message

Revision ID: first_data
Revises: d7071d7d01e8
Create Date: 2022-12-17 05:14:13.020063

"""
from alembic import op
from sqlalchemy import orm

from src.models import Provider, Flower, Customer, Contract, Order


# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = 'd7071d7d01e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind ()
    session = orm.Session (bind=bind)

    greenWorld = Provider(provider_code = "1", name = "greenWorld", adress = "ulica chego-to")
    loveFlower = Provider(provider_code = "2", name = "loveFlower", adress = "gde-to tut")

    session.add_all([greenWorld, loveFlower])
    session.flush()

    geocind = Flower(flower_code = "1", flowerName = "geocind", price = "100", provider_id = greenWorld.id)
    roza = Flower(flower_code = "2", flowerName = "roza", price = "140", provider_id = loveFlower.id)

    session.add_all([geocind, roza])
    session.flush()

    greenLand = Customer(customer_code = "1", name = "greenLand", adress = "chto-to gde-to", phone_number = "89234728911")
    zelenoeNechto = Customer(customer_code = "2", name = "zelenoeNechto", adress = "tuta", phone_number = "93485798347")

    session.add_all([greenLand, zelenoeNechto])
    session.flush()

    first = Contract(contract_code = "1", date_of_conf = "2001,9,9", date_of_exec = "2001,9,12", customers_id = greenLand.id)
    second = Contract(contract_code = "2", date_of_conf = "2001,9,10", date_of_exec = "2001,9,14", customers_id = zelenoeNechto.id )

    session.add_all([first, second])
    session.flush()

    rassada1 = Order(seedlings = "100000", contract_id = first.id, flower_id = geocind.id)
    rassada2 = Order(seedlings = "200000", contract_id = second.id, flower_id = roza.id)

    session.add_all([rassada1, rassada2])
    session.commit()


def downgrade() -> None:
    pass
