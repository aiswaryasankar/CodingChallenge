# Aiswarya Sankar
# Anagrams.py
# December 1, 2016


# This method will go through each word and convert it into a python dictionary mapping each letter to the number of times it occurs in the word

def createWordDict(word):
	wordDict = {}
	for letter in word:
		if letter not in wordDict:
			wordDict[letter] = 0 
		wordDict[letter] += 1

	return wordDict

# Optimized implementation

# Go through the list of words and create a dictionary of letters corresponding to each word in the list
def anagramsV2(contents):
	wordList = contents.split()

	# Dictionaries are mutable types and therefore can't be stored as keys in a dictionary
	# However I can work around this by turning the dictionary into a tuple of pairs which is immutable
	# Therefore I now have a dictionary where the keys are tuple pairs of the letters and their counts and the values are the words that have this letter breakdown

	masterDict = {}
	for word in wordList:
		wordDict = createWordDict(word.lower())
		tupleKey = tuple(sorted(wordDict.items()))

		if tupleKey not in masterDict:
			masterDict[tupleKey] = [word]
		else:
			masterDict[tupleKey].append(word)
	
	# Continuously reads in input until the user inputs an empty string
	while True:
		inputWord = str(raw_input()).lower()
		if len(inputWord) == 0:
			break

		inputWordDict = createWordDict(inputWord)
		inputWordTuple = tuple(sorted(inputWordDict.items()))

		# Checks if the word represented as a tuple of (character, count) pairs exists in the dictionary and returns the corresponding words
		if (inputWordTuple in masterDict):
			masterDict[inputWordTuple].sort()
			print (' '.join(masterDict[inputWordTuple]))
		else:
			print('-')


# Naive implementation
def anagrams(contents):
	wordList = contents.split()

	# masterDict holds all the words and their dictionary break ups
	masterDict = {}
	for word in wordList:
		wordDict = createWordDict(word)
		masterDict[word] = wordDict

	# Now I will read in the given word
	# Convert that word into a dictionary
	# Iterate through masterDict
	# Print out each word that is a match

	while True:
		inputWord = str(raw_input())
		if len(inputWord) == 0:
			break

		inputWordDict = createWordDict(inputWord)
		foundMatch = False
		for word in masterDict:
			if masterDict[word] == inputWordDict:
				foundMatch = True
				print(word),
		if not foundMatch:
			print('-'),
		print('')

import sys

f = open(sys.argv[1],"r")
contents = f.read()
f.close()
anagramsV2(contents)