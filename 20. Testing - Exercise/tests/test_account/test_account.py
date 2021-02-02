import unittest
from account import Account
import types


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.owner = 'Elena'
        self.amount = 100
        self.account = Account(self.owner, self.amount)

    def test_accountBalanceProperty_shouldReturnSumOfTransactionsAndAmount(self):
        self.assertEqual(self.account.balance, 100)
        self.account.add_transaction(50)
        self.assertEqual(self.account.balance, 150)

    def test_accountValidateTransaction_isStatic(self):
        self.assertTrue(isinstance(self.account.validate_transaction, types.FunctionType))

    def test_accountValidateTransaction_whenMoreThanZero_shouldAddTransactionAndReturnBalance(self):
        actual = Account.validate_transaction(self.account, 50)
        expected = f"New balance: 150"

        self.assertEqual(self.account._transactions, [50])
        self.assertEqual(actual, expected)

    def test_accountValidateTransaction_whenLessThanZero_shouldRaise(self):
        with self.assertRaises(ValueError) as context:
            Account.validate_transaction(self.account, -200)

        self.assertIsNotNone(context.exception)

    def test_accountAddTransaction_whenAmountIsInt_shouldAddAmount(self):
        self.account.add_transaction(50)

        actual = self.account._transactions
        expected = [50]
        self.assertEqual(actual, expected)

    def test_accountAddTransaction_whenAmountIsNotInt_shouldRaise(self):
        with self.assertRaises(ValueError) as context:
            self.account.add_transaction('invalid')

        self.assertIsNotNone(context.exception)

    def test_accountStr_shouldReturnString(self):
        actual = str(self.account)
        expected = "Account of Elena with starting amount: 100"

        self.assertEqual(actual, expected)

    def test_accountRepr_shouldReturnString(self):
        actual = repr(self.account)
        expected = "Account(Elena, 100)"

        self.assertEqual(actual, expected)

    def test_accountLen_shouldReturnTheLengthOfTransactions(self):
        self.account.add_transaction(50)

        actual = len(self.account)
        expected = 1
        self.assertEqual(actual, expected)

    def test_accountGetItem_whenValidIndex_shouldReturnItemAtIndex(self):
        self.account.add_transaction(50)

        actual = self.account[0]
        expected = 50
        self.assertEqual(actual, expected)

    def test_accountGetItem_whenInvalidIndex_shouldRaise(self):
        with self.assertRaises(IndexError) as context:
            self.account[10]

        self.assertIsNotNone(context.exception)

    def test_accountReversed_shouldReturnReversedTransactionsList(self):
        self.account.add_transaction(50)
        self.account.add_transaction(100)
        self.account.add_transaction(150)

        actual = list(reversed(self.account))
        expected = [150, 100, 50]
        self.assertEqual(actual, expected)

    def test_accountGreaterThan_whenBalanceIsGreater_shouldReturnTrue(self):
        account2 = Account('Maria', 200)

        self.assertGreater(account2, self.account)

    def test_accountLessThan_whenBalanceIsLess_shouldReturnTrue(self):
        account2 = Account('Maria', 200)

        self.assertLess(self.account, account2)

    def test_accountGreaterThanOrEqualTo_whenBalanceIsGreaterOrEqual_shouldReturnTrue(self):
        account2 = Account('Maria', 200)

        self.assertGreaterEqual(account2, self.account)

    def test_accountLessThanOrEqualTo_whenBalanceIsLessOrEqual_shouldReturnTrue(self):
        account2 = Account('Maria', 200)

        self.assertLessEqual(self.account, account2)

    def test_accountEqual_whenBalanceIsEqual_shouldReturnTrue(self):
        account2 = Account('Maria', 100)

        self.assertEqual(self.account, account2)

    def test_accountNotEqual_whenBalanceIsNotEqual_ShouldReturnTrue(self):
        account2 = Account('Maria', 200)

        self.assertNotEqual(self.account, account2)

    def test_accountAdd_shouldCreateNewAccountAndAddTransactions(self):
        account2 = Account('Maria', 100)
        self.account.add_transaction(50)
        account2.add_transaction(50)

        new_account = self.account + account2
        self.assertEqual(str(new_account), 'Account of Elena&Maria with starting amount: 200')
        self.assertEqual(new_account._transactions, [50, 50])


if __name__ == '__main__':
    unittest.main()
