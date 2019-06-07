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
