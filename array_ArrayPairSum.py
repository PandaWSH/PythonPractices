# Array Pair Sum
# --------------------
# Problem statement: Given an integer array, output all the unique pairs that sum 
# up to a specific value k.
# NOTE: "pair" means only 2 number
# ---------------------

# logistic: 
# 1. set up a tracker to store seen variables
# 2. for each element, if the difference btw that element and the target was in the seen set
# add the set(min, max) to the ouput set
# 3. after looping throuhg all element in the array, print the output set
def pair_sum(arr,k):
	if len(arr) < 2:
		return 

	# set for tracking
	seen = set()
	output = set()

	for i in arr:
		target = k - i

		if target not in seen:
			seen.add(i)

		else:
			output.add((min(i,target), max(i,target))) #keep the format of (min, max)

	return output