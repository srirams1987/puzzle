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

		
		

	def test_insert_and_find_word(self):
		"""
		Test simple trie function
		insert words 

		"""
		
		T = self.trie.Trie();
		#insert word
		T.insert( "word1")
		#find
		self.assertTrue(T.find_word("word1"))
		self.assertFalse(T.find_word("otherword"))

	def test_insert_find_multiple_words(self):
		"""
		Test to insert and find multiple words 
		also with numbers 
		"""
		T = self.trie.Trie()

		T.insert("word")
		T.insert("word-endings")
		T.insert("123")
		T.insert("12345678")

		self.assertTrue(T.find_word("word"))

		self.assertFalse(T.find_word("word-e"))
	
		self.assertTrue(T.find_word("word-endings"))

		self.assertTrue(T.find_word("123"))

		self.assertTrue(T.find_word("12345678"))

		self.assertFalse(T.find_word("123456"))

		self.assertFalse(T.find_word("123456789"))


	
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


		
	def test_negative(self):
		"""
		test for negative exceptions that are raised by Trie class
		"""
		T = self.trie.Trie()
		T.insert("words")
		#insert and find works only for words 
		self.assertRaises(TypeError, lambda: T.insert(234))
		self.assertRaises(TypeError, lambda: T.find_word(1234))
		#find_word_incremental works only for letter
		self.assertRaises(TypeError, lambda: T.find_word_incremental(1))
		self.assertRaises(ValueError, lambda: T.find_word_incremental("abcd"))



if __name__ == "__main__":
	
	unittest.main(verbosity=2)
	