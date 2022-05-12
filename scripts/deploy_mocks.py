from brownie import (
    MockV3Aggregator,
    network,
)
from scripts.helpful_scripts import (
    get_account,
)

DECIMALS = 8
INITIAL_VALUE = 200000000000


def deploy_mocks():
    print(f"Network: {network.show_active()}")
    account = get_account()
    MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})


def main():
    deploy_mocks()
