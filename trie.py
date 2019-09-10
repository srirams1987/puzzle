

import os
import sys


class TrieNode:
	"""
	a node in the trie data structure
	"""
	def __init__(self):
		"""
		constructor
		"""
		self.children = {}
		self.endNode = False


class Trie:
	"""
	A trie data structure to store the dictionary
	"""

	def __init__(self):
		"""
		Constructor: create a Trie Root Node.
		"""
		self._root = TrieNode()
		

	def insert(self, word):
		"""
		Insert word into the trie
		"""
		if not isinstance(word, str):
			raise(TypeError, "only string are allowed")


		tnode = self._root

		for letter in word:
			children = tnode.children
			if letter not in children.keys():
				children[letter] = TrieNode()
			
			tnode = children[letter]

		tnode.endNode = True

		


	def find_word(self, word):
		"""
		find a word in the trie
		"""

		if not isinstance(word, str):
			raise(TypeError, "only string are allowed")



		tnode = self._root
		findlist = []
		for letter in word:
			children = tnode.children

			if letter not in children:
				return False
			tnode = children[letter]
			findlist.append(letter)
		
		if tnode.endNode is True:
			return True
		
		return False

	def find_word_incremental(self, letter, node=None):
		"""
		find the word incrementally. 
		return the node where the letter is being found
		"""
		if not isinstance(letter, str):
			raise(TypeError, "only string are allowed")

		if len(letter)!=1:
			raise(ValueError, "letter(len==1) is required")

		if node is None:
			node = self._root
		children =  node.children
		if letter not in children:
			return None
		else:
			return children[letter]

			



