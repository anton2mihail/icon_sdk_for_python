import os
import unittest
import requests
requests.packages.urllib3.disable_warnings()
from icx.wallet.wallet import Wallet
from icx.utils import validate_wallet_info

TEST_DIR = os.path.dirname(os.path.abspath("tests/keystore_file/not_a_key_store_file.txt"))

uri = 'https://testwallet.icon.foundation/api/'


class TestGetWalletInfo(unittest.TestCase):

    def test0(self):
        """ Case to return the wallet address successfully.
        """
        password = "Adas21312**"
        keystore_file_path = os.path.join(TEST_DIR, "test_keystore.txt")

        try:
            wallet, _ = Wallet.open_keystore_file_of_wallet(keystore_file_path, password)
            wallet_info = wallet.get_wallet_info(uri)
            prefix = wallet_info['address'][0:2]
            self.assertEqual(prefix, "hx")
        except FileNotFoundError:
            self.assertFalse(True)

    def test1(self):
        """ Case to return the balance successfully.
        """
        password = "Adas21312**"
        keystore_file_path = os.path.join(TEST_DIR, "test_keystore.txt")

        try:
            wallet, _ = Wallet.open_keystore_file_of_wallet(keystore_file_path, password)
            wallet_info = wallet.get_wallet_info(uri)
            balance = wallet_info['balance']
            self.assertTrue(type(balance) == int)
        except FileNotFoundError:
            self.assertFalse(True)

    def test2(self):
        """ Case to return the wallet info in keystore file successfully.
        """
        password = "Adas21312**"
        keystore_file_path = os.path.join(TEST_DIR, "test_keystore.txt")

        try:
            wallet, _ = Wallet.open_keystore_file_of_wallet(keystore_file_path, password)
            wallet_info = wallet.get_wallet_info(uri)

            self.assertTrue(type(wallet_info) == dict)
        except FileNotFoundError:
            self.assertFalse(True)

    def test3(self):
        """ Case to return the correct form of wallet information.
        """
        password = "Adas21312**"
        keystore_file_path = os.path.join(TEST_DIR, "test_keystore.txt")

        try:
            wallet, _ = Wallet.open_keystore_file_of_wallet(keystore_file_path, password)
            wallet_info = wallet.get_wallet_info(uri)
            self.assertTrue(validate_wallet_info(wallet_info))
        except FileNotFoundError:
            self.assertFalse(True)

    def test4(self):
        """ Case to return the incorrect form of wallet information.
        """
        password = "Adas21312**"
        keystore_file_path = os.path.join(TEST_DIR, "test_keystore.txt")

        try:
            wallet, _ = Wallet.open_keystore_file_of_wallet(keystore_file_path, password)
            wallet_info = wallet.get_wallet_info(uri)
            del wallet_info["address"]
            self.assertFalse(validate_wallet_info(wallet_info))
        except FileNotFoundError:
            self.assertFalse(True)


if __name__ == "__main__":
    unittest.main()
