import requests
response = requests.get('https://quota.wohnheim.uni-kl.de/?lang=en')
incoming_add = response.text.find('incoming')+11
till_time_add = response.text.find('database')+14
incoming = response.text[incoming_add:incoming_add+4]
till_time = response.text[till_time_add:till_time_add+19]
print('Usage till '+str(till_time)+' is '+str(incoming))
