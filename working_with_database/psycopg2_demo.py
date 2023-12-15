import psycopg2
import psycopg2.extras
from icecream import ic
from dataclasses import dataclass

@dataclass
class Investment:
    id: int
    coin: str
    currency: str
    amount: float


connection = psycopg2.connect(
    host = 'localhost',
    database='manager',
    user='postgres',
    password='password'
)

# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
CREATE_INVESTMENTS_SQL = """
    create table if not exists investment (
        id serial primary key,
        coin varchar(32),
        currency varchar(3),
        amount real
    )
"""

cursor.execute(CREATE_INVESTMENTS_SQL)

add_bitcoin_investment = """
insert into investment (coin, currency, amount) values ('bitcoin', 'USD', 1.0);
"""

add_bitcoin_template = """
insert into investment (coin, currency, amount) values %s
"""

data = [
    ('ethereum', 'GBP', 10.0),
    ('dogecoin', 'EUA', 100.0)
]
cursor.execute(add_bitcoin_investment)
psycopg2.extras.execute_values(cursor, add_bitcoin_template, data)


select_bitcoin_investment = "select * from investment where coin = 'bitcoin'"
cursor.execute(select_bitcoin_investment)
data = cursor.fetchone()
print(data)

select_all_investments = "select * from investment"
cursor.execute(select_all_investments)
# data = cursor.fetchall()
# data = [dict(row) for row in cursor.fetchall()]
data = [Investment(**dict(row)) for row in cursor.fetchall()]
for investment in data:
    ic(investment.coin)

# ic(data)

cursor.close()
connection.commit()