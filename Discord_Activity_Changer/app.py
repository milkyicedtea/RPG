import os

from pypresence import Presence
import time
from dotenv import load_dotenv

load_dotenv()

client_id = int(os.getenv('client_id'))
print(client_id)
RPC = Presence(client_id)

RPC.connect()

RPC.update(state = 'Listening to her beautiful voice', large_image = 'guy_texting', large_text = 'test', details = 'Currently falling in love', buttons = [{'label': 'Repository link', 'url': 'https://github.com/milkyicedtea/Python-stuffy'}])

while True:
    time.sleep(15)
    print('15 seconds')