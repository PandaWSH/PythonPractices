# --------------------
# Recursion Practive
# --------------------

# -------- Problem 1 ---------
# factorial sum
def factsum(n):
	if n == 0:
		return 1
	else:
		return n * factsum(n-1)

# -------- Problem 2 ---------
# Given an integer, create a function which returns 
# the sum of all the individual digits in that integer. 
def fsum(x):
    # base case: single integer ( x//10 = 0)
    if x // 10 == 0:
        return x
    
    # otherwise
    else:
        return (x % 10) * fsum(x//10)
    
fsum(123) 

# -------- Problem 2 ---------
# NOTES: It aso has a lot of variation possibilities and we're 
# ignoring strict requirements here.

# Create a function called word_split() which takes in a string phrase and a set list_of_words. 
# The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. 
# You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
def word_split(phrase,list_of_words, output = None):
    if output is None:
        output = []
    
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            word_split(phrase[len(word):], list_of_words, output)
    return output
    pass
