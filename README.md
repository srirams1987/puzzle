
# Introduction
This repository has a automated way to solve a puzzle to find all the words from a grid of letters. The puzzle can be a random random of letters in which words can be formed by combining consecutive letters all 8 direction at any index. A dictionary of words is spplied as a txt file or can be supplied as input.

# How To
## puzzle_solver.py
``` bash
$ python puzzle_solver.py 15
```

## Run the tests:
``` bash
$ python test_puzzle.py
$ python test_trie.py
```
### To run all tests
```bash
$ python -m unittest discover test/.
```
## How to use the class in python 
``` python
>>> from puzzle import Puzzle
>>> puzzle_with_random = Puzzle(15)
>>> result = puzzle_with_random.solve()

>>> puzzle_with_known_puzzle_mat = Puzzle(puzzle_matrix=[<a-square_matrix-list-of-lists>], words_dictionary=["car","bus","bike","motor"])
>>> result = puzzle_with_known_puzzle_mat.solve()
```

# Contents:

1. trie.py : 

This class maintains the dictionary. It has methods to insert words into the dictionary and lookup words in the dictionary

2. puzzle.py :

This class has the algorithm to find all the words in the puzzle. The class constructor takes 3 options input argument
* size
* word_dictionary
* puzzle_matrix

"word_dictionary" argument is the predetermined list of words that can be given to the puzzle. If this is not supplied the class reads the "words.txt" that is supplied with the package. 
"puzzle_matrix" and "size" input arguments are related. If "puzzle_matrix" argument is not supplied, "size" is a required argument, else, "size" is extracted from the "size" of the "puzzle_matrix"

3. puzzle_solver.py

This is a script that wraps the puzzle class. This script takes 1 input argument, the "size" of the puzzle. 
``` bash
$ python puzzle_solver 10 
```

4. Test :
The test directory has the tests for Trie class and the Puzzle class. These tests uses python "unitests" package 
``` bash
$ python test_trie.py

$ python test_puzzle.py
```

Algorithm:
The Puzzle class uses trie instance to keep store all the words in the dictionary. Using a trie data structure makes it easy and quick to look up any word in the dictionary. The class constructor 
1. initializes the trie object and inserts all the words in the dictionary into the trie
2. creates the puzzle_matrix of the given size

The class has a "solve" method that solves for all the words in the puzzle_matrix at each index in all 8 directions, up, down , right, left, diag_up_left, diag_up_right, diag_down_right, diag_up_right in a recursive manner. 

The Trie class has a modified word look up method. This method incrementally looks up for the word in the trie one-letter-at-a-time. This strategy optimizes the search and makes is faster than multiple redundant lookups. 


Assumptions:
1. The implementation assumes that words.txt is always available in the current directory
2. The implementation assumes that the same cell in the puzzle can be in multiple words 
3. The implementation assumes that the puzzle_matrix is a square matrix, thus takes only one "size"  argument and constructs a square matrix is size-X-size dimensions
4. The implementation requires that the puzzle_matrix that is supplied as input is also a square_matrix
5. Tested with python 2.7

