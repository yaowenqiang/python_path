from pymongo import MongoClient

client = MongoClient() # connect to localhost on port 27017
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


large_amount_investments = investments.find({
    '$and': [
        {'amount': {'$gt': 100}},
        {'coin': 'bitcoin'}
    ]
})

watchlists.update_one({'_id': ''}, {
    '$push': {'coins': 'bitcoin'}
})

watchlists.update_one({'_id': ''}, {
    '$pull': {'coins': {'coin': 'bitcoin'}}
})

# investments.update_one({
#     'coin': 'bitcoin'
# }, {
#     '$inc': {'amount': 1}
# })








