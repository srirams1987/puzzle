import unittest
import os,sys,inspect

class TestTrie(unittest.TestCase):
	

	@classmethod
	def setUpClass(self):
		"""
		"""
		currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		parentdir = os.path.dirname(currentdir)
		sys.path.insert(0,parentdir) 
		import trie
		self.T = trie.Trie();

		
	@classmethod
	def tearDownClass(self):
		"""
		"""
		pass

	def test_insert_and_find_word(self):
		"""
		"""
		#insert word
		self.T.insert("word1")
		#find that word -> True
		self.assertTrue(self.T.find_word("word1"))
		#find some other word -> False
		self.assertFalse(self.T.find_word("otherword"))
		



if __name__ == "__main__":
	
	unittest.main(verbosity=2)
	pass