import contextio as c

CONSUMER_KEY = '9rr04zqo'
CONSUMER_SECRET = '1nUuKJkXFC03dbHD'

context_io = c.ContextIO(
    consumer_key=CONSUMER_KEY, 
    consumer_secret=CONSUMER_SECRET
)

params = { 'id': '551fa8ee8e079d711e8b4568'}
accounts = c.Account(context_io,params)
print(accounts)

