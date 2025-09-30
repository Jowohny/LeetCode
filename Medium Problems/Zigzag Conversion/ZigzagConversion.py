class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #create a number of lists based on the amount of rows
        #increment or decrement through zigzag list based on whether it has reached then number of rows or 0
        #go through entire list with a for loop 
        #concatenate all lists and return the result

        if len(s) <= numRows or numRows == 1:
            return s

        result = ""
        zigzag = [[] for i in range(numRows)]

        currId, ment = 0,1
        for i in s:
            zigzag[currId].append(i)
            if currId == 0:
                ment = 1
            elif currId == numRows-1:
                ment = -1
            currId += ment


        
        for zig in zigzag: 
            for i in zig:
                result += i

        return result

