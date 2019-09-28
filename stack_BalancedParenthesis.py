# --------------------
# Check balanced parenthesis
# --------------------

# Logistic I:
# 1. scan the list from lsft to the right
# 2. when see a open parenthesis, add to the stack
# 3. when see a closing one, check if the LAST open was corresponding one

def balanceCheck(A):
	if len(A)%2 != 0:
	 	return False

	# create open parenthesis set
	op = set("({[")

	# create tuple set of match pairs
	match = set([ ('{','}'), ('[',']'), ('(',')')])

	#python list operates the same way as a stack
	stack = []

	for pa in A:
		# meet a open parenthesis
		if pa in op:
			stack.append(pa)

		# meet a close parenthesis
		else:
			if len(stack) == 0:
				return False #there's no corresponding one

			last_open = stack.pop()
			if (last_open,pa) not in match:
				return False

	return len(stack) == 0