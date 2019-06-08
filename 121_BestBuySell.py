class Solution:
	'''
	For this problem, I have wrote six method but all have exceed running time
	So I analyzed each and debugged them each
	'''
    
    # Method 1, shared by others        
    def maxProfit(self, prices: List[int]) -> int:
        Min = float('inf'); 
        Max = 0
        
        for price in prices:
            Max = max(Max, price-Min)
            Min = min(price, Min)
         
        return Max

    # Method 2, my own worked one 92.48%
    # Min = Buy, Max = Sell 
    def maxProfit2(self, prices):
        if not prices:
            return 0
        else:
            Max = 0
            Min = prices[0]
            # for the rest elements in the list
            for i in prices[1::]:
            	# if the next element is greater than previous, consider about it
                if i > Min:
                    dif = i - Min
                    Max = max(Max, dif)
                # if not, pass and keep current Min, because it cannot bring 
                # available sell
                else:
                    Min = i
            return Max

    # Method 3, my own worked 72.68%
    # basically the same as method 1, but slower, the first two if
    # condition was actually not neccesary.
    def maxProfit(self, prices: List[int]) -> int:
        Min = float('inf')
        Max = 0
        if not prices or len(prices) == 1:
            return 0
        elif len(prices) == 2 and prices[0] > prices[1]:
            return 0
        else:
            for i in prices:
                Min = min(Min, i)
                Max = max(Max, i - Min)
            return Max

    # Method 3[wrong, need to debug], submisstion 1
    def maxProfit3(self, prices: List[int]) -> int:
        Max = 0
        for num in range(len(prices)):
            buy = prices[num]
            rest = prices[num::]
            Max_l = max([i - buy for i in rest])
            Max = max(Max,Max_l)
        if Max <= 0:
            return 0
        return Max