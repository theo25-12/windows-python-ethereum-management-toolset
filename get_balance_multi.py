from itertools import islice
from etherscan.accounts import Account
import json

NumOfLines = 10

def next_n_lines(file_opened, N):
    return [x.strip() for x in islice(file_opened, N)]

with open('api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']


with open('addr.txt', mode='r') as f:
    for i in range(0, NumOfLines):
        address = next_n_lines(f, 20)
        # you may also want to remove whitespace characters like `\n` at the end of each line
        address = [x.strip('\n') for x in address]
        api = Account(address=address, api_key=key)
        balances = api.get_balance_multiple()
        print(balances)
