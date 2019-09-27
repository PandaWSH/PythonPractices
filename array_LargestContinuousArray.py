def LargestSum(arr):

	if len(arr) == 0:
		return 0

	CurrentSum = MaxSum = arr[0]

	for num in arr[1:]:

		CurrentSum = max(CurrentSum + num, num)
		# CurrentSum is always the sum greater than the number just added
		# unless currentSum is more negative than the number
		# currentsum simply kept adding up, just update maxsum for result

		MaxSum = max(MaxSum, CurrentSum)

	return MaxSum

