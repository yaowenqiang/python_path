SQLite Usage Scenarios

+ SQLite does not use a server
+ Command line client opens a locally stored file
+ use as an embedded database
+ use during prototyping and development

install visual studio code extension

search sqlite


> sqlite3 
> .open test.db ( file will be created if not exists )
> create table investments(coin_id text, currency text, amount real);
> .tables
> .headers on
> .mode column 
> pragma table_info('investments')
> insert into investments values('bitcoin', 1.0, 'usd')

install rest book vistual studio extensition

> https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd


> pip install psycopg2-binary
> docker run --name postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -v /Users/yaojack/postgres/data:/var/lib/postgresql/data -d postgres


# sqlalchemy

https://docs.sqlalchemy.org/en/20/

> pip install sqlalchemy



