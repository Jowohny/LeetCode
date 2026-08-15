class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #every row starts and ends with a 1, and each inner number is the sum of the two numbers above it
        #so each new row can be built straight from the row we just made
        #start the result off with the very first row, which is just [1]
        #for each following row, add the neighboring pairs from the previous row to fill the middle
        #wrap that middle with a 1 on each end and tack the finished row onto the result
        #follows the same logic as its predecessor

        res = [1]

        #if the given row index is 0, just return the intialized result as it is already the other row index
        if rowIndex == 0:
            return res

        #build every row leading up to the given row index
        while rowIndex > 0:
						
            #every row opens with a 1
            row = [1]

            #each middle spot is the sum of the two numbers sitting above it in the previous row
            for j in range(1, len(res)):
                row.append(res[j - 1] + res[j])

            #every row closes with a 1
            row.append(1)

            #instead of storing the entire 2d pascals triangle array, just keep the latest one for reference
            res = row

            #decrease the amount of rows left to process
            rowIndex -= 1

        return res
