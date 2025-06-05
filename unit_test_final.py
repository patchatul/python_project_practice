import unittest
class MenuCoffee:
    def __init__(self):
        self.menu ={
            'espresso': 2.50,
            'latte': 2.50,
            'cappuccino': 2.50,
            'americano': 2.70
        }
    def get_price(self, item):
        return self.menu.get(item.lower())
    def add_item(self, item, price):
        self.menu[item.lower()] = price

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = MenuCoffee()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('latte'), 3.00) #FAILED 2.5 != 3.0
    
    def test_get_price_non_existing(self):
        self.assertIsNone(self.menu.get_price('frappe'))

    def test_add_item(self):
        self.menu.add_item('milk shake', 4.00)
        self.assertEqual(self.menu.get_price('milk shake'), 4.00)

if __name__ == '__main__':
    unittest.main()

