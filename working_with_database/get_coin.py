import requests
import sqlite3
import click
import datetime


@click.group
def cli():
    pass

CREATE_INVESTMENTS_SQL = """
create  table  if not exists investments (
    coin_id TEXT,
    currency TEXT,
    sell INT,
    amount REAL,
    date TIMESTAMP
);
"""

def get_coin_price(coine_id, currency):
    url = f'https://api.coingecko.com/api/v3/simple/prince?{coine_id}&vs_currencies={currency}'
    data = requests.get(url).json()
    coin_price = data[coin_id][currency]
    return coin_price

@click.command()
@click.option('--coin_id', default='bitcoin')
@click.option('--currency', default='usd')
def show_coin_price(coin_id, currency):
    coin_price = get_coin_price(coin_id, currency)
    print(f'The price of {coine_id} is {coin_price:.2f} {currency.upper()}')


@click.command()
@click.option('--coin_id', default='bitcoin')
@click.option('--currency', default='usd')
@click.option('--amount', type=float)
@click.option('--sell', is_flag=True)
def add_investment(coin_id, currency, amount, sell):
    sql = 'INSERT into investments VALUES(?,?,?,?,?);'
    values = (coin_id, currency, amount, sell, datetime.datetime.now())
    cursor.execute(sql, values)
    database.commit()

    if sell:
        print(f'Added sell of {amount} {coin_id}')
    else:
        print(f'Added buy of {amount} {coin_id}')



cli.add_command(show_coin_price)
cli.add_command(add_investment)



if __name__ == '__main__':
    database = sqlite3.connect('portfolio.db')
    cursor = database.cursor()
    cursor.execute(CREATE_INVESTMENTS_SQL)
    cli()
