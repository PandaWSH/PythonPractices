def luckySum(a, b, c):
  l = [a,b,c]
  summ,ind = 0,0
  while ind < 3:
  	if l[ind] == 13:
  		return summ
  	summ += l[ind]
  	ind += 1
  return summ

print(luckySum(13,1,1))

