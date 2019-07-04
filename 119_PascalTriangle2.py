class Solution:
    # my method 99.11% inspired by online method(2)88.34%
    def getRow(self, rowIndex: int) -> List[int]:
        # create initial row [1]
        # found the regularity that:
        # if row_i: [1]
        #                 [0,1] 
        #               + [1,0]
        #              --------
        # then row_i+1    [1,1]
        # apply the same rule to the rest

        row = [1]
        for i in range(rowIndex):
            # pattern
            a, b = [0]+row, row+[0]
            # however, because strings cannot be added in math way
            # each digit has to add relatively one by one
            row = [a[j]+b[j] for j in range(i+2)]
        return row

    def getRow2(self, rowIndex: int) -> List[int]:
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            row = [u+v for u, v in zip(row+[0], [0]+row)]
        return row




    # second time - DP method 36ms + 13.1MB (76.77% + 84.51%)
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1],[1,1]]
        if rowIndex == 0:            
            return result[0]
        if rowIndex == 1:
            return result[1]
        
        row = 2
        while row <= rowIndex:
            result.pop(0)
            result.append([1]*(row+1))
            for i in range(1,row):
                result[1][i] = result[0][i-1] + result[0][i]
            row += 1
        return result[1]