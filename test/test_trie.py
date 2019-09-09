import unittest
import os,sys,inspect

class TestTrie(unittest.TestCase):
	"""
	Unit test for trie class. 
	"""

	@classmethod
	def setUpClass(self):
		"""
		setup class. 
		Setup Path and import the trie class.
		"""
		currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		parentdir = os.path.dirname(currentdir)
		sys.path.insert(0,parentdir) 
		import trie
		self.trie = trie;

		
	@classmethod
	def tearDownClass(self):
		"""
		"""
		pass

	def test_insert_and_find_word(self):
		"""
		Test simple trie function
		insert words 

		"""
		#insert word
		T = self.trie.Trie();
		
		T.insert( "word1")
		#find that word -> True
		self.assertTrue(T.find_word("word1"))
		#find some other word -> False
		self.assertFalse(T.find_word("otherword"))
	
	def test_find_word_incremental(self):
		"""
		test for finding word incrementally
		"""
		T = self.trie.Trie()
		T.insert("python")
		T.insert("java")
		T.insert("Cpp")

		# Verify search for letters 
		# p y t h o n 
		# incrementally results in the right nodes that have the corresponding letters
		nextNode = T.find_word_incremental('p')
		self.assertFalse(nextNode is None)

		nextNode = T.find_word_incremental('y', nextNode)
		self.assertFalse(nextNode is None)

		nextNode = T.find_word_incremental('t', nextNode)
		self.assertFalse(nextNode is None)

		nextNode = T.find_word_incremental('h', nextNode)
		self.assertFalse(nextNode is None)

		nextNode = T.find_word_incremental('o', nextNode)
		self.assertFalse(nextNode is None)

		nextNode = T.find_word_incremental('n', nextNode)
		self.assertFalse(nextNode is None)
		#this node is the endNode 
		self.assertTrue(nextNode.endNode)

		#if the letter does not esixt at current node 
		nextNode = T.find_word_incremental('k', nextNode)
		self.assertTrue(nextNode is None)

		#if the letter does not esixt at root 
		nextNode = T.find_word_incremental('k')
		self.assertTrue(nextNode is None)


		







if __name__ == "__main__":
	
	unittest.main(verbosity=2)
	pass