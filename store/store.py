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
    store['channels'] = []
    channels = store['channels']

if 'itevents' in store:
    itevents = store['itevents']
else:
    store['itevents'] = []
    itevents = store['itevents']

if 'itc2go' in store:
    itc2go = store['itc2go']
else:
    store['itc2go'] = []
    itc2go = store['itc2go']


def save_store():
    with open(STORE_FILE, 'w') as f:
        f.write(json.dumps(store))

