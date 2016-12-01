
Anagrams.py

Implementation v2:

1) Running time of program:
	Offline: 

	Online:


2) How much memory:


Implementation v1:

1) Running time of program:
	
	Offline: 
		Linear time O(N) where N is the number of words given in the dictionary
	
	Online: 
		First we loop through each word in order to create the dictionaries. 	This will take linear time O(X) where X is the number of characters in the dictionary.
		Then we loop through the dictionary in order to check if the provided word matches any of the dictionaries in the masterDict.  This will perform N checks where N is the number of words in the dictionary.  I am using the built in equality check for dictionaries, therefore the runtime of this step is optimized by Python. It would have an upper bound of linear with respect to the number of characters in the word.

2) How much memory:
	Remembers each word O(X) where X is the total number of characters

