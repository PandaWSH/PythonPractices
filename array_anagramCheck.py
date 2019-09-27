# Anagram check (242)
# --------------------
# Problem statement: Given two strings, check to see if they are anagrams. 
# An anagram is when the two strings can be written using the exact same letters 
# (so you can just rearrange the letters to get a different phrase or word).
# ---------------------

# logistic I:
# 1. create a dictionary storing all element in array s, format{char:#, char:#, ...}
# 2. loop all element in array t, if that element in s_diction, char:#-1; if not, return false
# 3. loop through the s_diction, if any charactor with "# != 0", return false

def anagram(s, t):
	#remove space and convert to lowercase
	s = remove(' ','').lower()
	t = remove(' ','').lower()

	if len(s) != len(t):
		return false

	ss = {}
	tt = {}
	for i in s:
		if i not in ss:
			ss[i] = 1
		else:
			ss[i] += 1

	for i in t:
		if i not in ss:
			return false
		else:
			ss[i] -= 1

	for i in ss:
		if ss[i] != 0:
			return false

	return true



# logistic II:
# 1. same as previous method
# 2. create a diction using the same method but with array t
# 3. return if two diction were equal




