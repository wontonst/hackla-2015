import contextio as c
import requests
import json
from collections import Counter

CONSUMER_KEY = '9rr04zqo'
CONSUMER_SECRET = '1nUuKJkXFC03dbHD'

def main():
    context_io = c.ContextIO(
        consumer_key=CONSUMER_KEY, 
        consumer_secret=CONSUMER_SECRET
    )
    
    # params = { 'id': '551fa8ee8e079d711e8b4568'}
    # accounts = c.Account(context_io,params)
    accounts = context_io.get_accounts(email='tempforhacks@gmail.com')

    list = []
    
    for account in accounts:
        sync_result = account.post_sync()
        if(sync_result['success']):
            for message in account.get_messages():
                try :
                    message_body = message.get_body()
    				#print(message_body[0]['type'])
                    if(message_body[0]['type'] == 'text/plain'):
    					#print(len(message_body[0]['content']))
                        request_data = Counter()
                        email_body = message_body[0]['content']
                        request_data['txt'] = email_body
                        r = requests.post('http://sentiment.vivekn.com/api/text/',data=request_data)
    					#print('1')
                        if(r):
                            sentiment = r.json()['result']['sentiment']
                            list.append((message_body[0]['content'], sentiment))
    					    #this is where the email message body is being extracted, we can use this to get the emails
                except:
                    pass

    return list
    
if __name__ == '__main__':
    list = main()
