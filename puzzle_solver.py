from puzzle import Puzzle

import argparse


if __name__ == "__main__":
	"""
	Main Puzzle Solver 
	"""
	parser = argparse.ArgumentParser(description="All arguments to solve the puzzle")
	parser.add_argument('size', help='size of the puzzle', type=int)
	
	args = parser.parse_args()
	P = Puzzle( size=args.size)

	res = P.solve()
	print(res)