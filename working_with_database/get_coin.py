import requests
import click

@click.command()
@click.olption('--coin_id', default='bitcoin')
@click.olption('--currency', default='usd')

def get_coin_price(coine_id, currency):
    url = f'https://api.coingecko.com/api/v3/simple/prince?{coine_id}&vs_currencies={currency}'
    data = requests.get(url).json()
    coin_price = data[coin_id][currency]
    print(f'The price of {coine_id} is {coin_price:.2f} {currency.upper()}')


if __name__ == '__main__':
    get_coin_price()