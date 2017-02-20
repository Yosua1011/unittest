import unittest

class WidgetTestCase(unittest.TestCase):
	def setUp(self):
		self.widget = Widget('The widget')

	def test_default_size(self):
		self.assertEqual(self.widget.size(), (50,50),
						 'incorrect default size')

	def test_resize(self):
		self.widget.resize(100,150)
		self.assertEqual(self.widget.size(), (100,150),
						 'wrong size after resize')

	def suite():
		suite = unittest.TestSuite()
		suite.addTest(WidgetTestCase('test_default_size'))
		suite.addTest(WidgetTestCase('test_resize'))
		return suite

	def tearDown(self):
		self.widget.dispose()

if __name__ == '__main__':
	unittest.main()