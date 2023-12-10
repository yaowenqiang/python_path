import sqlite3
import datetime

database = sqlite3.connect('portfolio.db')

cursor = database.cursor()
create_table_query = """
create  table  investments (
    coin_id TEXT,
    currency TEXT,
    sell INT,
    amount REAL,
    date TIMESTAMP
);
"""

# cursor.execute(create_table_query)

investment = (
    'bitcoin',
    'usd',
    True,
    1.0,
    datetime.datetime.now()
)

cursor.execute(
    'INSERT into investments VALUES(?,?,?,?,?);',
    investment
)

database.commit()

result = cursor.execute('SELECT * from investments;')
all_rows = result.fetchall()


first_or_only_row = result.fetchone()
