'''import unittest
class tdd_python(unittest.TestCase):
    def test_banking_credit_methon_returns_correct_result(self):
        bank = banking()
final_bal = bank.credit(1000)
self.assertEqual(1000, final_bal)'''

'''import unittest
def add(a,b):
    return a + b 
class TestAdd (unnitest.TestCase):
    def test_add(self):
        result = add(10,20)
        self.assertEqual(result,30)

if __name__ == '__main__':
    unittest.main()'''

##USING UNITEST##

import unittest 
class BankAccount: 
    def init__(self, id):
        self. id = id
        self.balance = 0
def withdraw(self, amount):
    if self.balance >= amount:
        self.balance-= amount
        return True 
        return False
def deposit(self, amount):
    self.balance += amount 
    return True

    
class TestBankOperations(unittest.TestCase): 
    def test_insufficient_deposit(self):
# Arrange
        a = BankAccount(1)
        a. deposit( -100)
# ACt
        outcome = a.withdraw(200)
# Assert
        self.assertFalse(outcome) # in pytest - assert outcome ==False
