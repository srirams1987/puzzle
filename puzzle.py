
from trie import Trie
import random

class Puzzle:
	"""
	Create a Puzzle and solve for all the words in the puzzle
	"""
	def __init__(self, size=None, words_dictionary=None, puzzle_matrix=None):
		"""
		1. initalizes each cell with a letter at random
		2. reads the dictionary for all words
		3. constructs puzzle matrix

		"""
		
		#initialize the trie data structure
		self._trie = Trie()
		
		

		#puzzle_matrix can be initialized from the input or will be created at random.
		#this will make the algorithm testable 
		if puzzle_matrix is None:
			#create puzzle at random
			if size is None or size<=0 or (not isinstance(size, int)):
				raise(ValueError ,"size cannot be None, size must be >0 int")
			self._size = size
			self._puzzle = self._create_puzzle()
			
			
		else:
			#initialize puzzle from the input
			if self._is_puzzle_sq_matrix(puzzle_matrix) is True:
				self._size = len(puzzle_matrix)
				self._puzzle = puzzle_matrix
			else:
				raise(TypeError, "list must be a sq matrix(required)")

		#default get the words from words.txt
		#use the input list of words, this can be used for testing 
		if words_dictionary is None:
			self._words_file = "words.txt"
			self._read_words_from_dictionary()
		else:
			if isinstance(words_dictionary, list):
				self._all_words = words_dictionary
			else:
				raise(TypeError, 'words_dictionary must be a list of words')


		#insert the words in the trie
		self._initialize_trie()

		#result list 
		self.words_found_in_puzzle=[]
		



	#----- Private Methods ----#
	def _is_puzzle_sq_matrix(self, puzzle):
		"""
		Checks if the puzzle is a sq matrix(list of lists ) or not
		"""
		if not isinstance(puzzle, list):
			return False

		nrows = len(puzzle)
		for rows in puzzle:
			if not isinstance(rows, list):
				return False
			if len(rows) != nrows:
				return False

		return True


	def _create_puzzle(self):
		"""
		private method to create the puzzle
		each cell is a random letter a - z 
		"""
		result_puzzle = [] 
		for row in range(0, self._size):
			row = [chr(97+random.randint(0,25)) for index in range(0,self._size)]
			result_puzzle.insert(0,row)
		
		return result_puzzle


	def _read_words_from_dictionary(self):
		"""
		private method to read all words from the dictionary to get list of strings
		assumes the word-file is present in the current directory
		"""
		fid = open(self._words_file, "r")
		self._all_words = fid.read().splitlines()
		

	def _initialize_trie(self):
		"""
		initialize the trie and insert all the words into the trie
		"""
		for word in self._all_words:
			self._trie.insert(word)
	

	def _is_valid_rc(self, rind, cind):
		"""
		private method to validate the row index and the col index 
		"""
		if rind < 0 or cind < 0 or rind >= self._size or cind >= self._size: 
			return False
		else:
			return True


	def _solve_in_direction(self, row_ind, col_ind, direction, word="", node=None ):
		"""
		get the index in the "direction" given and find the word along that direction
		"""
		switcher ={
			"UP"    : [row_ind-1, col_ind],
			"DOWN"  : [row_ind+1, col_ind],
			"RIGHT" : [row_ind, col_ind+1],
			"LEFT"  : [row_ind, col_ind-1],
			"DIAG_UP_RIGHT"  : [row_ind-1, col_ind+1]	,
			"DIAG_UP_LEFT"   : [row_ind-1, col_ind-1],
			"DIAG_DOWN_RIGHT" : [row_ind+1, col_ind+1],
			"DIAG_DOWN_LEFT"  : [row_ind+1, col_ind-1],
				}
			
		nextNode, word = self._incremental_word_check(row_ind, col_ind, word, node)
		if nextNode is None:
			return
		self._solve_in_direction( switcher[direction][0], switcher[direction][1], direction ,word, nextNode)

	

	def _incremental_word_check(self, row_ind, col_ind, word, node):
		"""
		private method to incrementally check if the word exists in the Trie
		"""
		if not self._is_valid_rc( row_ind, col_ind):
			return None, None
		nextNode =  self._trie.find_word_incremental(self._puzzle[row_ind][col_ind], node) 
		if nextNode is None:
			return 	nextNode, word 
		word = str(word) + self._puzzle[row_ind][col_ind]
				 
		if nextNode.endNode is True:
			self.words_found_in_puzzle.append(word)
		
		return nextNode, word



	#----- Public Methods ----#
	def solve(self):
		"""
		solves and returns a list of all the words in the puzzel that are in the dictionary
		"""		
		self.words_found_in_puzzle = []
		for rind in range(0, self._size):
			for cind in range(0, self._size):
				self._solve_in_direction(rind, cind, "UP")
				self._solve_in_direction(rind, cind, "DOWN")
				self._solve_in_direction(rind, cind, "RIGHT")
				self._solve_in_direction(rind, cind, "LEFT")
				self._solve_in_direction(rind, cind, "DIAG_DOWN_LEFT")
				self._solve_in_direction(rind, cind, "DIAG_DOWN_RIGHT")
				self._solve_in_direction(rind, cind, "DIAG_UP_LEFT")
				self._solve_in_direction(rind, cind, "DIAG_UP_RIGHT")


		return self.words_found_in_puzzle

	def get_puzzle(self):
		"""
		Get the state of the puzzle
		"""
		return self._puzzle
		

	def get_dictionary(self):
		"""
		return the words in the dictionary
		"""
		return self._all_words

	def get_size(self):
		"""
		return the size of the puzzle
		"""
		return self._size



