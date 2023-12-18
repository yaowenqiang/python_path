from sqlalchemy import String, Numeric,Text, create_engine, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
import click
import requests


class Base(DeclarativeBase):
    pass

@click.group()
def cli():
    pass

# from icecream import ic
# engine = create_engine('sqlite:///demo_r.db')
engine = create_engine('postgresql://postgres:password@localhost:5432/manager')
Base.metadata.create_all(engine)


class Portfolio(Base):
    __tablename__ = 'portfolio'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())
    investments: Mapped[list['Investment']] = relationship(back_populates='portfolio')

    def __repr__(self):
        return f'<Portfolio name: {self.name}> with {len(self.investments)} investments'
    


class Investment(Base):
    __tablename__ = 'investment'
    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5,2))
    portfolio_id: Mapped[int] = mapped_column(ForeignKey('portfolio.id'))
    portfolio: Mapped['Portfolio'] = relationship(back_populates='investments')

    def __repr__(self):
        return f'<Investment coin: {self.coin}, currency: {self.currency}, amout: {self.amount}'

@click.command(help='Drop all tables in the database')
def clear_database():
    Base.metadata.drop_all(engine)
    print('Database cleared')

@click.command(help='Create a new investment and add it to a portfolio')
@click.option('--coin', prompt=True)
@click.option('--currency', prompt=True)
@click.option('--amount', prompt=True)
def add_investment(coin, currency, amount):
    with Session(engine) as session:
        stmt = select(Portfolio)
        all_portfolios = session.execute(stmt).scalars().all()
        for index, portfolio in enumerate(all_portfolios):
            print(f'{index + 1}: {portfolio.name}')
        
        portfolio_index = int(input('Select a portfolio: ')) - 1
        portfolio = all_portfolios[portfolio_index]

        investment = Investment(coin=coin, currency=currency, amount=amount)
        portfolio.investments.append(investment)
        session.add(portfolio)
        session.commit()

        print(f'Added new {coin} investment to {portfolio.name}')





@click.command(help='Create a new portfolio')
@click.option('--name', prompt=True)
@click.option('--description', prompt=True)
def add_portfolio(name, description):
    portfolio = Portfolio(name=name, description=description)
    with Session(engine) as session:
        session.add(portfolio)
        session.commit()
    print('Added new portfolio')


@click.command(help='View the investments for a portfolio')
def view_portfolio():
    with Session(engine) as session:
        stmt = select(Portfolio)
        all_portfolios = session.execute(stmt).scalars().all()
        for index, Portfolio in enumerate(all_portfolios):
            print(f'{index + 1}: {Portfolio.name}')
        
        portfolio_id = int(input('Select a portfolio:')) -1
        portfolio = all_portfolios[portfolio_id]

        investments = portfolio.investments

        coins = set([investment.coin for investment in investments])
        currencies = set([investment.currency for investment in investments])
        coin_prices = get_coin_price(coins, currencies)

        print(f'Investment in {portfolio.name}')
        for index, investment in enumerate(investments):
            coin_price = coin_prices[investment.coin][investment.currency.lower()]
            total_price = float(investment.amount) * coin_price
            print(f'{index + 1}: {investment.coin} {total_price:.2f} {investment.currency}')
        
        print('Prices provided for CoinGecko')



def get_coin_price(coins, currencies):
    coin_csv = ','.join(coins)
    currency_csv = ','.join(currencies)
    url = ''
    data = requests.get(url).json()
    return data

cli.add_command(clear_database)
cli.add_command(add_portfolio)
cli.add_command(view_portfolio)
cli.add_command(add_investment)

# Base.metadata.create_all(engine)

# bitcoin = Investment(coin='bitcoin', currency='USD', amount=1.0)
# ethereum = Investment(coin='ethereum', currency='GBP', amount=10.0)
# dogecoin = Investment(coin='dogecoin', currency='EUR', amount=100.0)

# portfolio1 = Portfolio(name='My Portfolio 1', description='My Description 1')
# portfolio2 = Portfolio(name='My Portfolio 2', description='My Description 2')
# bitcoin.portfolio = portfolio1

# portfolio1.investments.extend([ethereum, dogecoin])


# portfolio3 = Portfolio(name='Portfolio 3', description='Portfolio 3')
# bitcoin_2 = Investment(coin='bitcoin', currency='USD', amount=1.0)
# bitcoin_2.portfolio = portfolio3

# with Session(engine) as session:
#     session.add(bitcoin)
#     session.add(bitcoin_2)
#     session.add(portfolio2)
#     session.commit()

#     portfolio = session.get(Portfolio, 2)
#     print(portfolio)

#     for investment in portfolio.investments:
#         print(investment)
    
#     investment = session.get(Investment, 1)
#     print(investment.portfolio)

#     # join 
#     stmt = select(Investment).join(Portfolio)
#     print(stmt)

# subq = select(Investment).where(Investment.coin=='bitcoin').subquery()
# stmt = select(Portfolio).join(subq, Portfolio.id == subq.c.portfolio_id) # c means column
# print(stmt)
# portfolios = session.execute(stmt).scalars().all()
# print(portfolios)

if __name__ == '__main__':
    cli()