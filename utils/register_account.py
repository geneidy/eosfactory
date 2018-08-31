from  eosfactory import *
import argparse

def register_account(
    testnode_url, account_object_name):

    set_nodeos_address(testnode_url)
    if not verify_testnet():
        return

    create_wallet(file=True)
    create_master_account(account_object_name)


parser = argparse.ArgumentParser(description='''
Given an url and the account object name, get registration data.
Apply the data to the registration form of the testnet.
Enter 'go' when ready.

Example:
    python3 register_to_testnode.py https://api.kylin-testnet.eospace.io master
''')

parser.add_argument("testnode_url", help="An URL of a public node offering access to the testnet, e.g. http://88.99.97.30:38888")
parser.add_argument("account_object_name", help="The name of a Python variable which will hold reference the new account, e.g. master")

args = parser.parse_args()
register_account(
    args.testnode_url,
    args.account_object_name)