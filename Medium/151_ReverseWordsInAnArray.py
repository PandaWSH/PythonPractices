# Sentence Reverse
# --------------------
# Problem statement: 
# Reverse a sentence
# Notes: remove all leading or trailing whitespace
# ---------------------

# logistic I: 
# 1. sum up the first and the second array as two number
# 2. subtract and return the value
def rev_word(s):
	words = []
	length = len(s)
	space = [' '] #empty string

	i = 0

	while i < length:
		if s[i] not in space:
			word_start = i
			while i < length and s[i] not in space:#before it hits next space
				i += 1
			words.append(s[word_start:i]) 
			# NOTES: s[word_start:i] would be a element in an array, as a whole
		i += 1 # next word

	return " ".join(reversed(words))


# logistic II:
# using python functions
def reverseWords(self, s):
        return " ".join(reversed(s.split()))
        pass

