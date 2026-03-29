class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        #create a default dictionary and default it with empty lists
        diag = collections.defaultdict(list)

        #use this to add all values in diagonal order
        res = []

        #iterate through the 2D matrix with their corresding row and column
        #add the row and the column and use that as the unique identifier
        #in a diagonal, either the row increase and column decreases or the row decreases and the column decreases, meaning that the identifer stays constant for that spcific diagonal
        for r, l in enumerate(nums):
            for c, n in enumerate(l):
                
                #add the current value to the unique identifier
                diag[r+c].append(n)

        #grab all the keys from the default dictionary, it should typically should already come in order
        #for each key, get the associated list and reverse it, since we build it in reverse from celiing to wall
        for k in diag.keys():
            for v in reversed(diag[k]):

                #add the current value to the final list
                res.append(v)

        #return the diagonal traversed list
        return res
