from mongita import MongitaClientDisk

client = MongitaClientDisk()
db = client.portfolio # get or create the portfolio database
investments = db.investments  # get or create the investments collection

investments.insert_one({'coin_id': 'bitcoin', 'currency': 'usd', 'amount': 1.0})
investments.insert_many([
    {'coin_id': 'ethereum', 'currency': 'usd', 'amount': 10.0},
    {'coin_id': 'solana', 'currency': 'usd', 'amount': 25.0},
])

bitcoin_investments = investments.find({'coin_id': 'bitcoin'})
for i in bitcoin_investments:
    print(i)


first_bitcoin_investment = investments.find_one({'coin_id': 'bitcoin'})

all_investments = investments.find({})

no_investments = investments.find({'coin_id': 'dogecoin'})

updates = investments.update_many(
    {'coin_id': 'bitcoin'},
    {'$inc': {'amount': 0.1}}
)

delete = investments.delete_one(
    {'coin_id': 'bitcoin'},
)










