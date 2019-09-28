# String Compression
# --------------------
# Problem statement: 
# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. 
# For this problem, you can falsely "compress" strings of single or double letters. 
# For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
# ---------------------

# logistic I: 
# 1. create a diction {}
# 2. loop through all element, if x in dition, diction[x]+=1, else, diction[x]=0
# 3. convert dition into string
# NOTES: not sure if output format correct

def StringCompress(s):
    if len(s) == 0:
        return ""

    diction = {}
    for i in s:
        if i not in diction:
            diction[i] = 0
        else:
            diction[i] += 1

    v = diction.values()
    k = diction.keys()
    
    kk = [key for key in k]
    vv = [value for value in v]
    
    result = []
    for i in range(len(kk)):
        result.append(kk[i])
        result.append(vv[i])
    
    result = str(result).replace('[','')
    result = str(result).replace(']','')
    result = str(result).replace("'",'')
    result = str(result).replace(",",'')
    
    return result

# logistic II:
# compression without checking algorithm
# NOTES: this method only works for sorted array
def StringCompress(s):
	result = "" #run
	l = len(s)

	if l == 0:
		return result #empty string

	if l == 1:
		return s 

	cnt = 1 #counter
	i = 1 #index

	while i < l:
		if s[i] == s[i-1]:
			cnt += 1
		else:
			result = result + s[i-1] + str(cnt)
			# update the result while counting
			cnt = 1
			# reset the counter and start another one
		i += 1

	# put everything together, because the last element was not counted yet
	result = result + s[i-1] + str(cnt)

	return result

# For example 'AAaa'
# - under while condition:
# 	s[1] == s[0]:
# 		cnt = 1+1 = 2
# 		i = 1+1 = 2
# 	s[2] != s[1]:
# 		r = "" + s[1] + cnt = "A2"
# 	s[3] == s[2]:
# 		cnt = 2
# 		i = 3+1 = 4
# - out of the while condition:
# 	r = "A2" + "a" + "2"

# For example 'Abc'
# - under while condition:
# 	s[1] != s[0]:
# 		r = "" + s[0] + cnt = "A1"
# 		cnt = 1 #no change
# 	s[2] != s[1]:
# 		r = "A1" + s[1] + cnt = "A1b1"
# 		cnt = 1 #no change
# - out of the while condition:
# 	r = "A1b1" + "c" + "1"




 












