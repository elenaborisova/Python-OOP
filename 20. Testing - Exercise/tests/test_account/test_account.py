import unittest
from account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.owner = 'Elena'
        self.amount = 100
        self.account = Account(self.owner, self.amount)

    def test_accountBalanceProperty_shouldReturnSumOfTransactionsAndAmount(self):
        self.assertEqual(self.account.balance, 100)
        self.account.add_transaction(50)
        self.assertEqual(self.account.balance, 150)

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

        actual = reversed(self.account)
        expected = [150, 100, 50]
        self.assertEqual(actual, expected)



