import unittest
from json_ex import check_char_count

class TestJsonEx (unittest.TestCase):

	def test_check_char_count(self)
		self.assertEqual(check_char_count('AA'), 'AA count passes')
        	self.assertEqual(check_char_count('AAA'), 'AAA count FAILS')

if __name__ == '__main__':
    unittest.main()

