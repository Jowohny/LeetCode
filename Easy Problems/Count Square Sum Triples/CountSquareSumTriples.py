class Solution:
    def countTriples(self, n: int) -> int:
        #create a dictionary with all the squares in the range of 1 to n
        squares = {c*c:c for c in range(1,n+1)}

        #keep a counter
        res = 0

        #test all the possibilities a's and b's within the ranges
        for a in range(1, n+1):
            for b in range(1, n+1):
                #if the sum of the current a square and b square has a value in the hashmap, then add 1 to the counter
                if (a*a)+(b*b) in squares:
                    res += 1

        #after testing all possible values, return the amount of possible satisfactory values
        return res 