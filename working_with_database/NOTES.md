SQLite Usage Scenarios

+ SQLite does not use a server
+ Command line client opens a locally stored file
+ use as an embedded database
+ use during prototyping and development

install visual studio code extension


> sqlite3 
> .open test.db ( file will be created if not exists )
> create table investments(coin_id text, currency text, amount real);
> .tables
> .headers on
> .mode column 
> pragma table_info('investments')


