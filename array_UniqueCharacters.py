# Unique Characters in An Array
# --------------------
# Problem statement: Given an integer array, output all the unique pairs that sum 
# Given a string,determine if it is compreised of all unique characters. 
# or example, the string 'abcde' has all unique characters and should return True. 
# The string 'aabcde' contains duplicate characters and should return false.

# ---------------------

# logistic I: 
# 1. use python set() shortcut function
def unique_ch(a):
	return len(set(u)) == len(u)

# logistic II:
# 1. create an empty set recording seen characters
# 2. check through every element in the array
# 3. if in the seen set, return false
# 4. else, return true after finish the for-loop
def unique_ch(a):

	chars = set()

	for i in a:
		if i in chars: 
			return False
		else:
			chars.add(i)

	return True
