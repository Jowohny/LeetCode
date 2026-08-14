class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #every row starts and ends with a 1, and each inner number is the sum of the two numbers above it
        #so each new row can be built straight from the row we just made
        #start the result off with the very first row, which is just [1]
        #for each following row, add the neighboring pairs from the previous row to fill the middle
        #wrap that middle with a 1 on each end and tack the finished row onto the result

        res = [[1]]

        #build every row after the first one
        for i in range(1, numRows):

            prev = res[-1]
						
            #every row opens with a 1
            row = [1]

            #each middle spot is the sum of the two numbers sitting above it in the previous row
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])

            #every row closes with a 1
            row.append(1)

            res.append(row)

        return res
