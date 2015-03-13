import requests
import hashlib
import json
url = 'http://localhost:8002/mirror/payment/'

SECRET = 'secret'
MIRROR_ID = 1
issue_id = 1
user_id = 2
sign = hashlib.md5(SECRET+str(user_id)).hexdigest()
data = {'user_id': user_id, 'issue_id': issue_id, 'mirror_id': MIRROR_ID, 'sign': sign}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
oo = requests.post(url, data=json.dumps(data), headers=headers).content

print oo
