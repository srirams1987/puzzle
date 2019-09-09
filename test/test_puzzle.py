import unittest
import os,sys,inspect


class TestPuzzle(unittest.TestCase):
	

	@classmethod
	def setUpClass(self):
		"""
		set up PATH and initialize the test cases 
		"""
		currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		parentdir = os.path.dirname(currentdir)
		sys.path.insert(0,parentdir) 

		from puzzle import Puzzle
		self.Puzzle = Puzzle;
		self.test_words = ["car","bus","bar","kind","auto","acm","aid","aim"]
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
		self.test_down_diag = [["a","b","a"],
		                       ["c","i","t"],
						       ["m","i","d"]]

		
	@classmethod
	def tearDownClass(self):
		"""
		"""
		pass

	def test_horozontal_right(self):
		"""
		Test for find word along the RIGHT direction 
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_horizontal )
		self.assertEqual(P.get_size(), 3);
		self.assertEqual(P.get_dictionary(), self.test_words)
		self.assertEqual(P.get_puzzle(), self.test_puzzle_horizontal)
		res = P.solve();
		self.assertEqual(res, ['car', 'bus', 'bar'])

	def test_vertical_down(self):
		"""
		Test for find word along the LEFT direction 
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_vertical )
		
		res = P.solve();
		self.assertEqual(res, ["auto"])


	def test_diagonal(self):
		"""
		Test for find word along the DIAGONAL DOWN RIGHT direction 
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_diag )
		
		res = P.solve();
		self.assertEqual(res, ["kind"])

	def test_downdiag(self):
		"""
		Test for find word along the DIAGONAL DONW RIGHT and DIAGONAL DOWN LEFT and DOWN direction 
		"""
		P = self.Puzzle(None, self.test_words, self.test_down_diag )
		
		res = P.solve();
		self.assertEqual(res, ["acm", "aid","aim"])


	@unittest.skip(1)
	def test_puzlle_all_direction():
		"""
		"""

	def test_negative(self):
		"""
		"""
		self.assertRaises(ValueError, lambda: self.Puzzle(-10))

		self.assertRaises(ValueError, lambda: self.Puzzle(0))

		self.assertRaises(ValueError, lambda: self.Puzzle(10.10))

		self.assertRaises(TypeError, lambda: self.Puzzle(puzzle_matrix=[1,2,3,4]))
		

	


if __name__=="__main__":
	unittest.main(verbosity=2)
	pass