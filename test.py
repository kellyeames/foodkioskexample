import unittest
from item import Item
from order import Order
from employee import Employee

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item=item(1, 'burger', 4.00)
    
    def test_string(self):
        self.AssertEqual(str(self.test), self.test.itemname)

class Order(unittest.TestCase):
    def test_size(self):
        self.detail=OrderDetail('burger')

class Employee(unittest.TestCase):
    def test_string(self):
        self.AssertEqual(str(self.test), self.test.empployeename)

