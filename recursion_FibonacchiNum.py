# --------------------
# Recursion - Fibonnaci Number 
# --------------------
# check online: search "five ways for solving Fibonnaci number"

# Method I: Recursion, O(n^2)
def fib_r(n):
	# base case
	if n == 0 or n == 1:
		return n
	# recursive case
	else:
		return fib_r(n-1) + fib_r(n-2)

# Method II: Iteration
def fib_i(n):
	a,b = 0,1

	for i in range(n):

		a,b = b, a+b

	return b


# Method III: Dynamic -- with known n
n = 12 #some number
cache = [None] * (n+1)
def fib_d(n):
	# base case
	if n == 0 or n == 1:
		return n

	# check cache
	if cache[n] != None:
		return cache[n]

	# keep setting cache
	cache[n] = fib_d(n-1) + fib_d(n-2)

	return cache[n]