import unittest

from project.books.models import Book
from project.customers.models import Customer
from project.loans.models import Loan


XSS = '<script>alert(1)</script>'


class ValidatorTest(unittest.TestCase):
    def test_correct_data(self):
        self.assertEqual(Book('Lalka', 'Bolesław Prus', 1890, '5days').name, 'Lalka')
        self.assertEqual(Customer('Łukasz Żółć', 'Gdańsk', 30).city, 'Gdańsk')
        self.assertEqual(Loan('Jan Kowalski', 'Lalka', None, None, 'Prus', 1890, '5days').book_name, 'Lalka')

    def test_xss_is_rejected(self):
        with self.assertRaises(ValueError):
            Book(XSS, 'Author', 2000, '5days')
        with self.assertRaises(ValueError):
            Customer('Jan Kowalski', XSS, 30)
        with self.assertRaises(ValueError):
            Loan(XSS, 'Lalka', None, None, 'Prus', 1890, '5days')


if __name__ == '__main__':
    unittest.main()
