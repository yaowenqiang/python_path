from sqlalchemy import String, Numeric,Text, create_engine, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
# from icecream import ic
engine = create_engine('sqlite:///demo_r.db')

class Base(DeclarativeBase):
    pass

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

Base.metadata.create_all(engine)

bitcoin = Investment(coin='bitcoin', currency='USD', amount=1.0)
ethereum = Investment(coin='ethereum', currency='GBP', amount=10.0)
dogecoin = Investment(coin='dogecoin', currency='EUR', amount=100.0)

portfolio1 = Portfolio(name='My Portfolio 1', description='My Description 1')
portfolio2 = Portfolio(name='My Portfolio 2', description='My Description 2')
bitcoin.portfolio = portfolio1

portfolio1.investments.extend([ethereum, dogecoin])


portfolio3 = Portfolio(name='Portfolio 3', description='Portfolio 3')
bitcoin_2 = Investment(coin='bitcoin', currency='USD', amount=1.0)
bitcoin_2.portfolio = portfolio3

with Session(engine) as session:
    session.add(bitcoin)
    session.add(bitcoin_2)
    session.add(portfolio2)
    session.commit()

    portfolio = session.get(Portfolio, 2)
    print(portfolio)

    for investment in portfolio.investments:
        print(investment)
    
    investment = session.get(Investment, 1)
    print(investment.portfolio)

    # join 
    stmt = select(Investment).join(Portfolio)
    print(stmt)

subq = select(Investment).where(Investment.coin=='bitcoin').subquery()
stmt = select(Portfolio).join(subq, Portfolio.id == subq.c.portfolio_id) # c means column
print(stmt)
portfolios = session.execute(stmt).scalars().all()
print(portfolios)


