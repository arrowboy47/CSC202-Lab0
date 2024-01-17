import unittest
import lab0

class TestProd(unittest.TestCase):

    def test_def(self):
        result = lab0.Product(name='shirt', price=50, amount=1)
        self.assertEqual(result.name, 'shirt')
        self.assertEqual(result.price, 50)
        self.assertEqual(result.amount, 1)

    def test_getPrice(self):
        # 10-99 items
        p1 = lab0.Product("textbook",80, 10)
        self.assertEqual(p1.getPrice(), 720)

        # <5 items
        p2 = lab0.Product("shirt", 50, 5)
        self.assertEqual(p2.getPrice(), 250)

        # 100+ items
        p3 = lab0.Product("history book", 50, 100)
        self.assertEqual(p3.getPrice(), 4000)

    def test_make_purchase(self):
        # textbook test
        p1 = lab0.Product("textbook",80, 10)
        self.assertEqual(p1.make_purchase(1000, 10), 280)

        # shirt test 
        p2 = lab0.Product("shirt", 50, 5)
        self.assertEqual(p2.make_purchase(1000, 5), 750)


class TestConvert(unittest.TestCase):
    # testing converter class creation
    def test_name(self):
        # incorrect unit name
        self.assertRaises(ValueError, lab0.Converter, 1, 'liters')

        measure = lab0.Converter(1, 'm')
        self.assertEqual(measure.unit, 'm')
    
    # testing conversion method



#allows us to run unit tests from command line with just: "python tests0.py"
if __name__ == '__main__':
    unittest.main()