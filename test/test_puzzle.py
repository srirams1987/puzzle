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

		from puzzle import Puzzle
		self.Puzzle = Puzzle;
		self.test_words = ["car","bus","bar","kind","auto"]
		self.test_puzzle_horizontal = [["c","a","r"],
					 ["b","u","s"],
					 ["b","a","r"]]
		self.test_puzzle_diag = [["k","","",""],
					["","i","",""],
					["","","n",""],
					["","","","d"]]
		self.test_puzzle_vertical = [["a","","",""],
						["u","","",""],
						["t","","",""],
						["o","","",""]]

		
	@classmethod
	def tearDownClass(self):
		"""
		"""
		pass

	def test_horozontal(self):
		"""
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_horizontal )
		

	def test_vertical(self):
		"""
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_vertical )
		
	def test_diagonal(self):
		"""
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_diag )


	def test_negativeTest(self):
		"""
		"""

		pass



if __name__=="__main__":
	unittest.main(verbosity=2)
	pass