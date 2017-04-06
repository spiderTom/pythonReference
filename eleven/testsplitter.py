import splitter
import unittest
	
	
class TestSplitFunction(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def testsimplestring(self):
		r = splitter.split('GOOG 100 490.50')
		self.assertEqual(r, ['GOOG', '100', '490.50'])
		print "testsimplestring pass"
	def testtypeconvert(self):
		r = splitter.split('GOOG 100 490.50', [str, int, float])
		self.assertEqual(r, ['GOOG', 100, 490.5])
		print "testtypeconvert pass"
	def testdelimiter(self):
		r = splitter.split('GOOG,100,490.50', delimiter=',')
		self.assertEqual(r, ['GOOG','100','490.50'])
		print "testdelimiter pass"
		
		
if __name__ == '__main__':
	unittest.main()
		
