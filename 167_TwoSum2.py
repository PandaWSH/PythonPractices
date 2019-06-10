class Solution:

    #此方法没有办法处理相同的数相加
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cla = {}
        for i,e in enumerate(numbers):
            cla[e] = i
            
        pos = 0
        while pos < len(numbers):
            left = numbers[pos]
            dif = target - left
            print('left:',left, 'dif:',dif)
            if dif in cla:
                a=  [pos+1,numbers.index(dif)+1]
                return a
            pos += 1

    # time exceed        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for i,e in enumerate(numbers):
        num = numbers[i+1::]
        dif = target - e
        print('dif:',dif)
        try:
            a = num.index(dif) + (i+1)
            print('a',a)
            return [i+1,a+1]
        except:
            b = 1

    # ----------------------------------- dictionary method --------------------------------------
    # 优化了第一种解法，让dictionary变成了dynamic的，gradually increase
    # 省时省空间，而且如果出现了两个一样的数字&target等于两数之和也不怕，因为是在判断之后才把被判断的数加进去的
    def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i
    

    # ----------------------------------- two pointer method --------------------------------------       
    #good method shared online <two pointers>
    '''
    this method used the property of the sorted array
    分别从这个的list的两端开始，这样也快
    p1左边min value，p2右边max value
    if sum(p1+p2) > target, means we need smaller p2, so move p2 one place left
    elif sum(p1+p2) < target, means we need a greater p1, so move p1 one place right
    elif sum(p1+p2) == target, found
    '''
    def twoSum(self, numbers, target):
        p1 = 0
        p2 = len(numbers) - 1
        while p2 > p1:
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            elif numbers[p1] + numbers[p2] == target:
                return [p1 + 1, p2 + 1]
        else:
            return None

    # similar to last solution
    def twoSum1(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1








