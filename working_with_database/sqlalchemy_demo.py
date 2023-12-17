from sqlalchemy import String, Numeric, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
# from icecream import ic
engine = create_engine('sqlite:///demo.db')

class Base(DeclarativeBase):
    pass


class Investment(Base):
    __tablename__ = 'investment'
    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5,2))

    def __repr__(self):
        return f'<Investment coin: {self.coin}, currency: {self.currency}, amout: {self.amount}'

Base.metadata.create_all(engine)

bitcoin = Investment(coin='bitcoin', currency='USD', amount=1.0)
ethereum = Investment(coin='ethereum', currency='GBP', amount=10.0)
dogecoin = Investment(coin='dogecoin', currency='EUR', amount=100.0)

with Session(engine) as session:
    session.add(bitcoin)
    session.add_all([ethereum, dogecoin])
    session.commit()

    # stmt = select(Investment)
    # print(stmt)


    stmt = select(Investment).where(Investment.coin == 'bitcoin')
    # print(stmt)
    # bitcoin = session.execute(stmt).scalar_one()
    # bitcoin = session.execute(stmt).scalar_one()
    # print(bitcoin)
    investment = session.get(Investment, 1)
    print(investment)

    stmt = select(Investment).where(Investment.amount > 5)
    investments = session.execute(stmt).scalars().all()
    print(investments)
    for i in investments:
        print(i)

    # stmt = select(Investment).where(Investment.coin == 'foocoin')
    # session.execute(stmt).scalar_one()


    bitcoin = session.get(Investment, 1)
    bitcoin.amount = 1.234
    print(session.dirty)
    session.commit()
    print(bitcoin)

    dogecoin = session.get(Investment, 4)
    print(session.deleted)
    session.delete(dogecoin)
    session.commit()


    




