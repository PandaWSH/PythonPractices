# --------------------
# Recursion - reverse string 
# --------------------

# Given a string, write a function that uses recursion to output a list 
# of all the possible permutations of that string.

# For example, given s='abc' the function should return ['abc', 'acb', 
# 'bac', 'bca', 'cab', 'cba']

# Note: If a character is repeated, treat each occurence as distinct, for 
# example an input of 'xxx' would return a list with 6 "versions" of 'xxx'

# AVAILABLE LIBRARY: itertools library
def permute (s):
	out = []
	# base case
	if len(s) == 1:
		out = [s]

	
	else:
		# for every letter in the string
		for ind, let in enumerate(s):
			# for every permutation in step 2 and step 3
			for perm in permute( s[:ind] + s[ind+1:] ):
				# add it to the output
				out += [let + perm]

	return out

