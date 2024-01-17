import unittest
import lab0

class TestProd(unittest.TestCase):

    def test_def(self):
        result = lab0.Product(name='shirt', price=50, amount=1)
        self.assertEqual(result.name, 'shirt')
        self.assertEqual(result.price, 50)
        self.assertEqual(result.amount, 1)

    


    def test_getPrice(self):
        p1 = lab0.Product("textbook", 80, 10)
        self.assertEqual(p1.getPrice(), 720)



    def test_make_purchase(self):



#class TestConvert(unittest.TestCase):



#allows us to run unit tests from command line with just: "python tests0.py"
if __name__ == '__main__':
    unittest.main()