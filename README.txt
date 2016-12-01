
Anagrams.py

Implementation v2:
	Motivation: The previous implementation was taking up unnecessary memory since anagrams were storing the same dictionary multiple times. I wanted to find a way to only store each dictionary once.  Dictionaries can't be keys but I changed it to an immutable sorted list.

1) Running time of program:
	Offline: 
		Linear time O(N) where N is the number of words given in the dictionary

	Online:
		O(N) + O(W) where N is the number of words in dictionary and W is the number of words that you are looking up. Each word lookup takes constant time.
		Loop through all the words and create dictionaries O(N) where N is the number of words
		When you input a new word, first create the dictionary.  Then we have constant look up time because we are storing the word make up as the dictionary key.  Looking up a key in a dictionary takes constant time.  Thus the online step 

2) How much memory:
	We are storing each of the N words in the dictionary.  We are also storing at most N tuple pairs of their letter counts.  This is a constant factor scaling with regard to N so therefore we have a space complexity of O(N). In the best case the dictionary will only have one key.  

Implementation v1:

1) Running time of program:
	
	Offline: 
		Linear time O(N) where N is the number of words given in the dictionary
	
	Online: 
		First we loop through each word in order to create the dictionaries. 	This will take linear time O(X) where X is the number of characters in the dictionary.
		Then we loop through the dictionary in order to check if the provided word matches any of the dictionaries in the masterDict.  This will perform N checks where N is the number of words in the dictionary.  I am using the built in equality check for dictionaries, therefore the runtime of this step is optimized by Python. It would have an upper bound of linear with respect to the number of characters in the word.

2) How much memory:
	Remembers each word O(X) where X is the total number of characters

