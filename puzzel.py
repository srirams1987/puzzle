
from trie import Trie

class Puzzel:
	"""
	Create a Puzzel and solves for all the words in the puzzel
	"""
	def __init__(self, size):
		"""
		constructs the puzzel and initalizes teach cell with a letter at random
		1. reads the dictionary for all words
		2. constructs puzzel matrix

		"""
		self._trie = Trie();
		
		self._read_words_from_dictionary()

		self._initialize_trie()

		pass

	def _read_words_from_dictionary():
		"""
		"""
		self._all_words
		pass

	def _intialize_trie():
		"""
		"""
		for word in self._all_words:
			self._trie.insert(word)
		
		pass
		

	def solve(self):
		"""
		solves and returns a list of all the words in the puzzel that are in the dictionary
		"""
		pass


if __name__ == "__main__":
	P = Puzzel(4);
	P.solve()

