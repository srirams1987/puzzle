

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
		self.children = {};
		self.endNode = False


class Trie:
	"""
	A trie data structure to store the dictionary
	"""

	def __init__(self):
		"""
		Constructor: create a Trie Root Node.
		"""
		self.__root = TrieNode()
		

	def insert(self, word):
		"""
		Insert word into the trie
		"""
		tnode = self.__root

		for letter in word:
			#print(letter)
			children = tnode.children
			if letter not in children.keys():
				children[letter] = TrieNode();
			
			tnode = children[letter];

		tnode.endNode = True;

		


	def find_word(self, word):
		"""
		find a word in the trie
		"""

		tnode = self.__root
		findlist = [];
		for letter in word:
			#print(letter)
			children = tnode.children
			#print(children)
			if letter not in children:
				return False
			tnode = children[letter];
			findlist.append(letter)
		
		if tnode.endNode is True:
			return True;
		
		return False;


if __name__ == "__main__":
	T = Trie();
	T.insert("word1")
	T.find_word("word1")


