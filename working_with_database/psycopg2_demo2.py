from dataclasses import dataclass
from icecream import ic

import psycopg2
import psycopg2.extras
import click
import csv
# import requests

@dataclass
class Investment:
    id: int
    coin: str
    currency: str
    amount: float

def get_connection():
    connection = psycopg2.connect(
        host = 'localhost',
        database='manager',
        user='postgres',
        password='password'
    )
    return connection

@click.group()
def cli():
    pass



@click.command()
@click.option('--currency')
def view_investment(currency):
    stmt = f"""
        select * from  investment 
    """
    if currency is not None:
        stmt += f" where currency = '{currency.lower()}'"
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(stmt)
    data = [Investment(**dict(row)) for row in cursor.fetchall()]
    for investment in data:
        ic(investment)
    cursor.close()
    connection.close()


@click.command()
@click.option('--coin', prompt=True)
@click.option('--currency', prompt=True)
@click.option('--amount', prompt=True)
def new_investment(coin, currency, amount):
    stmt = f"""
        insert into investment (coin, currency, amount) 
        values (
            '{coin.lower()}',
            '{currency.lower()}',
            '{amount}'
        )
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    cursor.close()
    connection.close()

    print(f'Added investment fro {amount} {coin} in {currency}')

@click.command()
@click.option('--filename', prompt=True)
def import_investment(filename):
    stmt = "insert into investment(coin, currency, amount) values %s"
    connection = get_connection()
    cursor = connection.cursor()

    with open(filename, 'r') as f:
        coin_reader = csv.reader(f)
        rows = [[x.lower() for x in row[1:]] for row in coin_reader]

    psycopg2.extras.execute_values(cursor, stmt, rows)
    connection.commit()
    cursor.close()
    connection.close()

    print(f'Added {len(rows)} investments')


cli.add_command(new_investment)
cli.add_command(import_investment)
cli.add_command(view_investment)

if __name__ == '__main__':
    cli()



# cursor = connection.cursor()
# CREATE_INVESTMENTS_SQL = """
#     create table investment (
#         id serial primary key,
#         coin varchar(32),
#         currency varchar(3),
#         amount real
#     )
# """

# cursor.execute(CREATE_INVESTMENTS_SQL)

# add_bitcoin_investment = """
# insert into investment (coin, currency, amount) values ('bitcoin', 'USD', 1.0);
# """

# add_bitcoin_template = """
# insert into investment (coin, currency, amount) values %s
# """

# data = [
#     ('ethereum', 'GBP', 10.0),
#     ('dogecoin', 'EUA', 100.0)
# ]
# cursor.execute(add_bitcoin_investment)
# psycopg2.extras.execute_values(cursor, add_bitcoin_template, data)

# cursor.close()
# connection.commit()