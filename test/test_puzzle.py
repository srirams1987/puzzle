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
		self.test_words = ["car","bus","bar","kind","auto","ace","aid"]
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
						       ["e","i","d"]]

		
	@classmethod
	def tearDownClass(self):
		"""
		"""
		pass

	def test_horozontal(self):
		"""
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_horizontal )
		self.assertEqual(P.get_size(), 3);
		self.assertEqual(P.get_dictionary(), self.test_words)
		self.assertEqual(P.get_puzzle(), self.test_puzzle_horizontal)
		res = P.solve();
		self.assertEqual(res, ['car', 'bus', 'bar'])

	def test_vertical(self):
		"""
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_vertical )
		
		res = P.solve();
		self.assertEqual(res, ["auto"])


	def test_diagonal(self):
		"""
		"""
		P = self.Puzzle(None, self.test_words, self.test_puzzle_diag )
		
		res = P.solve();
		self.assertEqual(res, ["kind"])

	def test_downdiag(self):
		"""
		"""
		P = self.Puzzle(None, self.test_words, self.test_down_diag )
		
		res = P.solve();
		self.assertEqual(res, ["ace", "aid"])


	@unittest.skip(1)
	def test_puzlle_all_direction():
		"""
		"""
		

	@unittest.skip(1)	
	def test_negativeTest(self):
		"""
		"""
		self.assertRaises(self.Puzzle(None, [""], ["","",""]))
		pass



if __name__=="__main__":
	unittest.main(verbosity=2)
	pass