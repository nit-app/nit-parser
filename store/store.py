import json

STORE_FILE = 'store/store.json'

with open(STORE_FILE, 'r') as f:
    content = f.read()
    if not content:
        store = {}
    else:
        store = json.loads(content)

if 'channels' in store:
    channels = store['channels']
else:
    channels = []
