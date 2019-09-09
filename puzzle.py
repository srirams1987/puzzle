
from trie import Trie
import random

class Puzzle:
	"""
	Create a Puzzle and solve for all the words in the puzzle
	"""
	def __init__(self, size=None, words_dictionary=None, puzzle_matrix=None):
		"""
		constructs the puzzel and initalizes teach cell with a letter at random
		1. reads the dictionary for all words
		2. constructs puzzle matrix

		"""
		
		#initialize the trie data structure
		self.__trie = Trie();
		
		

		#puzzle_matrix can be initialized from the input or will be created at random.
		#this will make the algorithm testable 
		if puzzle_matrix is None:
			#create puzzle at random
			if size is None or size<=0 or (not isinstance(size, int)):
				raise(ValueError ,"size cannot be None, size must be >0 int")
			self.__size = size;
			self.__puzzle = self.__create_puzzle()
			
			
		else:
			#initialize puzzle from the input
			if self.__is_puzzle_sq_matrix(puzzle_matrix) is True:
				self.__size = len(puzzle_matrix)
				self.__puzzle = puzzle_matrix
			else:
				raise(TypeError, "list must be a sq matrix(required)")

		#default get the words from words.txt
		#use the input list of words, this can be used for testing 
		if words_dictionary is None:
			self.__words_file = "words.txt"
			self.__read_words_from_dictionary()
		else:
			self.__all_words = words_dictionary;

		#insert the words in the trie
		self.__initialize_trie()

		self.words_found_in_puzzle=[];
		


	def __is_puzzle_sq_matrix(self, puzzle):
		"""
		Checks if the puzzle is a sq matrix or not
		"""
		if not isinstance(puzzle, list):
			return False;

		nrows = len(puzzle);
		for rows in puzzle:
			if not isinstance(rows, list):
				return False;
			if len(rows) != nrows:
				return False

		return True;


	def __create_puzzle(self):
		"""
		private method to create the puzzle
		"""
		result = [] ;
		for row in range(0, self.__size):
			row = [chr(97+random.randint(0,25)) for x in range(0,self.__size)]
			result.insert(0,row)
		
		return result


	def __read_words_from_dictionary(self):
		"""
		private method to read all words from the dictionary to get list of strings
		"""
		fid = open(self.__words_file, "r")
		self.__all_words = fid.read().splitlines();
		

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
		

	def get_dictionary(self):
		"""
		return the words in the dictionary
		"""
		return self.__all_words

	def get_size(self):
		"""
		return the size of the puzzle
		"""
		return self.__size


	def __is_valid_rc(self, rind, cind):
		"""
		private method to validate the row index and the col index 
		"""
		if rind < 0 or cind < 0 or rind >= self.__size or cind >= self.__size: 
			return False;
		else:
			return True;

	
	def __solve_up(self, rind, cind, word="", node=None):
		"""
		find words in the UP direction 
		"""
		
		nextNode, word = self.__incremental_word_check(rind, cind, word, node)
		if nextNode is None:
			return
		self.__solve_up( rind-1, cind, word, nextNode)

	def __solve_down(self, rind, cind , word="", node=None):
		"""
		find words in the DOWN direction 
		"""
		
		nextNode, word= self.__incremental_word_check(rind, cind, word, node)
		if nextNode is None:
			return
		self.__solve_down( rind+1, cind, word, nextNode)

		


	def __solve_right(self, rind, cind, word="", node=None):
		"""
		find words in the RIGHT direction
		"""
		
		nextNode, word = self.__incremental_word_check(rind, cind, word, node)
		if nextNode is None:
			return
		self.__solve_right(rind, cind+1, word, nextNode)

	

	def __solve_left(self, rind, cind, word="", node=None):
		"""
		find words in the LEFT direction
		"""
		
		nextNode, word = self.__incremental_word_check(rind, cind, word, node)
		if nextNode is None:
			return
		self.__solve_left( rind, cind-1,word,  nextNode)

	

	def __solve_diag_up_right(self, rind, cind, word="", node=None):
		"""
		find words in the DIAGONAL UP RIGHT direction
		"""
		
		nextNode, word = self.__incremental_word_check(rind, cind, word, node)
		if nextNode is None:
			return
		self.__solve_diag_up_right( rind-1, cind+1, word, nextNode)


	def __solve_diag_up_left(self, rind, cind, word="", node=None):
		"""
		find words in teh DIAGONAL UP LEFT direction
		"""
		
		nextNode, word = self.__incremental_word_check(rind, cind, word, node)
		if nextNode is None:
			return
		self.__solve_diag_up_left( rind-1, cind-1, word, nextNode)


	def __solve_diag_down_right(self, rind, cind, word="", node=None):
		"""
		find words in the DIAGONAL DOWN RIGHT direction 
		"""
		
		nextNode, word = self.__incremental_word_check(rind, cind, word, node)
		if nextNode is None:
			return
		self.__solve_diag_down_right( rind+1, cind+1,word, nextNode	)


	def __solve_diag_down_left(self, rind, cind, word="", node=None):
		"""
		find words in the DIAGONAL DOWN LEFT direction
		"""
		
		nextNode, word = self.__incremental_word_check(rind, cind, word, node)
		if nextNode is None:
			return
		self.__solve_diag_down_left( rind+1, cind-1, word, nextNode)

	def __solve_backwards(self, rind, cind, word="", node=None):
		"""
		find words in the BACKWARDS
		"""

		
		nextNode, word = self.__incremental_word_check(rind, cind, word, node)
		if nextNode is None:
			return
		self.__solve_backwards( rind, cind-1, word, nextNode)


	def __incremental_word_check(self, rind, cind, word, node):
		"""
		private method to incrementally check if the word exists in the Trie
		"""
		if not self.__is_valid_rc( rind, cind):
			return None, None
		nextNode =  self.__trie.find_word_incremental(self.__puzzle[rind][cind], node) 
		if nextNode is None:
			return 	nextNode, word 
		word = str(word) + self.__puzzle[rind][cind]
				 
		if nextNode.endNode is True:
			self.words_found_in_puzzle.append(word)
			#print word
		
		return nextNode, word
		pass

	def solve(self):
		"""
		solves and returns a list of all the words in the puzzel that are in the dictionary
		"""
			
		
		for rind in range(0, self.__size):
			for cind in range(0, self.__size):
				#print(rind, cind) 
				self.__solve_right(rind, cind)
				self.__solve_left(rind, cind)
				self.__solve_up(rind, cind)
				self.__solve_down(rind, cind)
				self.__solve_diag_up_right(rind, cind)
				self.__solve_diag_up_left(rind, cind)
				self.__solve_diag_down_right(rind, cind)
				self.__solve_diag_down_left(rind, cind)
				self.__solve_backwards(rind, cind)

		return self.words_found_in_puzzle


