import psycopg2
import psycopg2.extras

connection = psycopg2.connect(
    host = 'localhost',
    database='manager',
    user='postgres',
    password='password'
)

cursor = connection.cursor()
CREATE_INVESTMENTS_SQL = """
    create table investment (
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

cursor.close()
connection.commit()