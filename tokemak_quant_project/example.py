import os

from dotenv import load_dotenv
from web3 import Web3

default_provider_url = "https://eth-mainnet.g.alchemy.com/v2/_gg7wSSi0KMBsdKnGVfHDueq6xMB9EkC"


def main():
    load_dotenv()
    provider_url = os.getenv('MAINET', default_provider_url)
    w3 = Web3(Web3.HTTPProvider(provider_url))

    if w3.isConnected():
        block_number = w3.eth.block_number
        personal_balance = w3.eth.get_balance('danielpartida.eth')
        personal_ether = w3.fromWei(personal_balance, 'ether')
        latest_block = w3.eth.get_block('latest')


if __name__ == '__main__':
    main()
