import os

import pandas as pd
from dotenv import load_dotenv
from web3 import Web3

default_provider_url = "https://eth-mainnet.g.alchemy.com/v2/_gg7wSSi0KMBsdKnGVfHDueq6xMB9EkC"


def read_pool_data(file: str = '../data/uni_v2_sushi_pools.csv') -> pd.DataFrame:
    """
    Read pool data and filter data where ETH (WETH) are one of the tokens
    :param file: file name with its location, assumes that tokenmak_quant_project/ is working directory
    :return: pd.DataFrame with filtered data
    """
    data = pd.read_csv(file)

    data = data[(data.token0_symbol == 'WETH') | (data.token1_symbol == 'WETH')]

    return data


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

    pool_data = read_pool_data()

    main()
