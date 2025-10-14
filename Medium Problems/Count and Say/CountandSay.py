class Solution:
    def countAndSay(self, n: int) -> str:
        #start with "1" as the base case
        #loop n - 1 times to build each sequence of numbers
        #use a pointer to move through the current sequence
        #count how many times the same digit repeats back to back
        #when a new digit appears, add how many times there were along with the the digit to the new string
        #update the next sequence with the newly created one
        #return the final sequence after looping n times


        res = "1"
        for _ in range(n - 1):
            newS = ""
            i = 0
            while i < len(res):
                count = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    count += 1
                    i += 1
                newS += str(count) + res[i]
                i += 1
            res = newS
        return res

