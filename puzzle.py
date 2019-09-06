
from trie import Trie
import random

class Puzzle:
	"""
	Create a Puzzle and solves for all the words in the puzzle
	"""
	def __init__(self, size):
		"""
		constructs the puzzel and initalizes teach cell with a letter at random
		1. reads the dictionary for all words
		2. constructs puzzel matrix

		"""
		self.__size = size+1
		
		self.__trie = Trie();
		
		self.__words_file = "words.txt"
		
		self.__read_words_from_dictionary()

		self.__initialize_trie()

		self.__puzzle = self.__create_puzzle()

		print(self.__puzzle)




	def __create_puzzle(self):
		"""
		private method to create the puzzle
		"""
		result = [] ;
		for row in range(1, self.__size):
			row = [chr(97+random.randint(0,25)) for x in range(1,self.__size)]
			result.insert(0,row)
		
		return result


	def __read_words_from_dictionary(self):
		"""
		private method to read all words from the dictionary to get list of strings
		"""
		fid = open(self.__words_file, "r")
		self.__all_words = fid.readlines();
		

	def __initialize_trie(self):
		"""
		initialize the trie and insert all the words into the trie
		"""
		for word in self.__all_words:
			#print(word)
			self.__trie.insert(word)
		
		


	def solve(self):
		"""
		solves and returns a list of all the words in the puzzel that are in the dictionary
		"""
		pass


if __name__ == "__main__":
	P = Puzzle(10);
	P.solve()

