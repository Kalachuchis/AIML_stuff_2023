from unittest import TestCase
from InsecurityBank import InsecurityBank


INITIAL_AMOUNT = 10000


class TestHandler(TestCase):
    def setUp(self) -> None:
        self.no_balance = InsecurityBank()
        self.with_balance = InsecurityBank(INITIAL_AMOUNT)

    def test_new_account(self):
        self.assertEqual(self.no_balance.check_balance(), 0)
        self.assertEqual(self.with_balance.check_balance(), INITIAL_AMOUNT)

    def test_negative_account(self):
        with self.assertRaises(ValueError) as err_context:
            error_account = InsecurityBank(-100)
        print(err_context.exception)
        self.assertEqual(
            str(err_context.exception), "Input should be a nonnegative number"
        )

    def test_negative_withdraw(self):
        with self.assertRaises(ValueError) as err_context:
            self.with_balance.withdraw(-500)
        print(str(err_context.exception))
        self.assertEqual(
            str(err_context.exception), "Input should be a positive number"
        )

    def test_negative_deposit(self):
        with self.assertRaises(ValueError) as err_context:
            self.with_balance.deposit(-500)
        print(str(err_context.exception))
        self.assertEqual(
            str(err_context.exception), "Input should be a positive number"
        )

    def test_withdrawal(self):
        self.with_balance.withdraw(5000)
        self.assertEqual(
            self.with_balance.check_balance(), (INITIAL_AMOUNT - (5000 * 1.3))
        )

    def test_insufficient(self):
        with self.assertRaises(ValueError) as err_context:
            self.no_balance.withdraw(500)
        print(str(err_context.exception))

    def test_deposit(self):
        self.no_balance.deposit(500)
        self.assertEqual(self.no_balance.check_balance(), 500)
