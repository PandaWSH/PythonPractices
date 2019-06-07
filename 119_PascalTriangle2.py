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