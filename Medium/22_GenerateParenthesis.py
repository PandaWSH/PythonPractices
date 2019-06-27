class Solution:
	# method 1 backtracking: 40 ms + 13.4 MB (86.04% + 58.60%)
	def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

    # method 2 stack: 44 ms + 13.2 MB (55.41% +90.42%)
    def generateParenthesis(self, n):
	    res = []
	    s = [("(", 1, 0)]
	    while s:
	        x, l, r = s.pop()
	        if l - r < 0 or l > n or r > n:
	            continue
	        if l == n and r == n:
	            res.append(x)
	        s.append((x+"(", l+1, r))
	        s.append((x+")", l, r+1))
	    return res

	# method 3: backtracking: 44 ms + 13.4 MB
    def generateParenthesis(self, n):
	    def paren(left, right, curr, res):
			# 'evaluate current string
			# if we are out of brackets to add, we must be at a valid string
		    if left == 0 and right == 0:
			    res.append(curr)
			    return

			# recursive call: add either open or close
			# if adding open bracket is valid
		    if left > 0:
				# add open bracket, decr count
			    paren(left-1, right, curr + "(", res)

			# if adding close bracket is valid
		    if right > left:
				# add close bracket, decr count
			    paren(left, right-1, curr + ")", res)

		    return res
		# end paren()

	    res = paren(n, n, '', [])

	    return res