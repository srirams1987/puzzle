import unittest
import os,sys,inspect

class TestPuzzle(unittest.TestCase):
	

	@classmethod
	def setUpClass(self):
		"""
		"""
		currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		parentdir = os.path.dirname(currentdir)
		sys.path.insert(0,parentdir) 

		
	@classmethod
	def tearDownClass(self):
		"""
		"""
		pass

	def test_insert_and_find_word(self):
		"""
		"""



if __name__=="__main__":
	unittest.main(verbosity=2)
	pass