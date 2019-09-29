# --------------------
# Recursion - reverse string 
# --------------------
def revString(x):
	result = ''
	# base case
	if len(x) <= 1:
		return x

	# repeat
	else:
		return result + x[-1] + revString([:-1])

# ------------------------
# instead of appending new element, it could be 
# always inserting at the begining
def revString(x):
	# base case
	if len(x) <= 1:
		return x

	# repeat
	else:
		return revString(x[1:]) + x[0]
