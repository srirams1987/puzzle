import unittest
import os,sys,inspect


class TestPuzzle(unittest.TestCase):
	"""
	Unit test for Puzzle class 
	"""

	@classmethod
	def setUpClass(self):
		"""
		set up PATH and initialize the test cases 
		"""
		currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		parentdir = os.path.dirname(currentdir)
		sys.path.insert(0,parentdir) 

		from puzzle import Puzzle
		self.Puzzle = Puzzle
		self.test_words = ["car","bus","bar","kind","auto","acm","aid","aim"]
		self.test_puzzle_horizontal = [["c","a","r"],
					 ["b","u","s"],
					 ["b","a","r"]]
		self.test_puzzle_diag = [["k","a","a","a"],
					["a","i","a","a"],
					["a","a","n","a"],
					["a","a","a","d"]]
		self.test_puzzle_vertical = [["a","c","a","c"],
						["u","1","1","1"],
						["t","2","2","2"],
						["o","3","3","3"]]
		self.test_down_diag = [["a","b","a"],
		                       ["c","i","t"],
						       ["m","i","d"]]

		

	def test_horozontal_right(self):
		"""
		Test for find word along the RIGHT direction 
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_horizontal )
		self.assertEqual(P.get_size(), 3);
		self.assertEqual(P.get_dictionary(), self.test_words)
		self.assertEqual(P.get_puzzle(), self.test_puzzle_horizontal)
		res = P.solve()
		self.assertEqual(res, ['car', 'bus', 'bar'])

	def test_vertical_down(self):
		"""
		Test for find word along the LEFT direction 
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_vertical )
		
		res = P.solve()
		self.assertEqual(res, ["auto"])


	def test_diagonal(self):
		"""
		Test for find word along the DIAGONAL DOWN RIGHT direction 
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_diag )
		
		res = P.solve()
		self.assertEqual(res, ["kind"])

	def test_downdiag(self):
		"""
		Test for find word along the DIAGONAL DONW RIGHT and DIAGONAL DOWN LEFT and DOWN direction 
		"""
		P = self.Puzzle(None, self.test_words, self.test_down_diag )
		
		res = P.solve()
		self.assertEqual(res, ["acm", "aid","aim"])


	@unittest.skip(1)
	def test_puzzle_all_direction():
		"""
		"""

	def test_negative(self):
		"""
		Test for negative cases of the Puzzle constructor 
		"""
		self.assertRaises(ValueError, lambda: self.Puzzle(-10))

		self.assertRaises(ValueError, lambda: self.Puzzle(0))

		self.assertRaises(ValueError, lambda: self.Puzzle(10.10))

		self.assertRaises(TypeError, lambda: self.Puzzle(puzzle_matrix=[1,2,3,4]))
		

	


if __name__=="__main__":
	unittest.main(verbosity=2)
	pass