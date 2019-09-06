
from trie import Trie
import random

class Puzzle:
	"""
	Create a Puzzle and solves for all the words in the puzzle
	"""
	def __init__(self, size=None, words_dictionary= None, puzzle_matrix=None):
		"""
		constructs the puzzel and initalizes teach cell with a letter at random
		1. reads the dictionary for all words
		2. constructs puzzle matrix

		"""
		
		self.__trie = Trie();
		
		#default get the words from woords.txt
		#use the input list of words, this can be used for testing 
		if words_dictionary is None:
			self.__words_file = "words.txt"
			self.__read_words_from_dictionary()
		else:
			self.__all_words = words_dictionary;

		self.__initialize_trie()


		#puzzle_matrix can be initialized from the input of will be created at random.
		if puzzle_matrix is None:
			#create puzzle at random
			self.__puzzle = self.__create_puzzle()
			if size is  None:
				raise("size cannot be None")

			self.__size = size+1;

		else:
			#initialize puzzle from the input
			if self.__is_puzzle_sq_matrix(puzzle_matrix) is True:
				self.__size = len(puzzle_matrix)
				self.__puzzle = puzzle_matrix
			else:
				raise(TypeError, "list sq matrix is required")

		print(self.__puzzle)


	def __is_puzzle_sq_matrix(self, puzzle):
		"""
		"""
		return True;


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
			self.__trie.insert(word)
	
	def get_puzzle(self):
		"""
		Get the state of the puzzle
		"""
		return self.__puzzle
		

	def get_all_words(self):
		"""
		"""
		return self.__all_words


	def solve(self):
		"""
		solves and returns a list of all the words in the puzzel that are in the dictionary
		"""
		pass


if __name__ == "__main__":

	P = Puzzle(10);
	P.solve()

