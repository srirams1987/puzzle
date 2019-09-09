from puzzle import Puzzle

import argparse


if __name__ == "__main__":
	"""
	Main Puzzle Solver 
	"""
	parser = argparse.ArgumentParser(description="All argumnets to solve the puzzle")
	parser.add_argument('--size', help='size of the puzzle', type=int)
	#parser.add_argument('--puzzle_matrix', help='pre formed puzzle matrix', type=list)
	#parser.add_argument('--words_dictionary', help='words for the dictionary', type=list)

	args = parser.parse_args()
	P = Puzzle( size=args.size)

	res = P.solve()
	print(res)