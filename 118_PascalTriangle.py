class Solution:
    # method one
    def generate1(self, num_rows):
        # create empty list
        result = []
        
        #if input is zero, return empty
        if num_rows == 0:
            return result
        else:
            for r in range(num_rows):
                #create the row list with #numb_rows elements 
                row = [None for i in list(range(r+1))]
                # make the 1st and last as 1
                row[0] = 1
                row[-1] = 1
                # the rest of element in betweem
                for j in range(1,len(row)-1):
                    #prev row previous position + prev row current position
                    row[j] = result[r-1][j-1] + result[r-1][j]
                #append this row after each row is finished    
                result.append(row)
        return result


    # method two
    def generate2(self, num_rows):
        if num_rows == 0:
            return []
        else:
            # create #nums_input of elements         
            result = [0] * num_rows
            for r in range(num_rows):            
                if r == 0: #first row
                    result[r]= [1]
                elif r == 1: #second row
                    result[r] = [1,1]
                else: #starting from the third row(r = 2)
                    #create the same number of element as the row number
                    result[r] = [0] * (r + 1)
                    result[r][0] = 1
                    result[r][-1] = 1
                    for c in range(1,r):
                        result[r][c] = result[r-1][c-1] + result[r-1][c]
                    
        return result

    # second time - 32ms +13.3MB [91.89% + 8.10%] similar to method two
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return[[1],[1,1]]
        result = [[1],[1,1]]
        row = 3
        while row <= numRows:            
            thisRow = [1]*row
            print(thisRow)
            for i in range(1,row-1):
                thisRow[i] = result[row-2][i-1] + result[row-2][i]            
            result.append(thisRow)
            row+=1
        return result

    # second time - 36ms + 13.2MB (75.39% + 40.41%)
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [[1 for i in range(j+1)]for j in range(numRows)] #occupyingi space
        for i in range(2,numRows,+1):
            for j in range(1,i,+1):

                nums[i][j] = nums[i-1][j-1] + nums[i-1][j]

        return nums
