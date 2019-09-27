# Find Missing Element
# --------------------
# Problem statement: 
# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element. 
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# ---------------------

# logistic I: 
# 1. sum up the first and the second array as two number
# 2. subtract and return the value
def finder(arr1, arr2):
	s1, s2 = 0, 0
	for i in arr1:
		s1 += i
	for j in arr 2:
		s2 += i 
	return s1 - s2

# logistic II:
# 1. sum up the first array using for loop
# 2. delet every element from the sum
# 3. return the rest value of sum as the result 
def finder(arr1, arr2):
	s = 0
	for i in arr1:
		s += i
	for j in arr2:
		s -= i
	return s
