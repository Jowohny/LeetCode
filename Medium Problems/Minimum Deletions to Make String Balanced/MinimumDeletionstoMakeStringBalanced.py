class Solution:
    def minimumDeletions(self, s: str) -> int:

        #keep track of how many deletions we need to balance the given string
        res = 0

        #record how many bs there are along the current iteration of the string
        b = 0

        #iterate through each character in the string
        for c in s:

            #if the current letter is a b, add 1 to the total amount
            if c == 'b':
                b += 1

            #assuming we get to this point since the current character isn't a b, it is presumed that it is an a
            #this checks if b is non-zero
            #so if we have any amount of bs and we come across an a, add 1 to the total amount of deletions and take away 1 from the total amount of bs
            elif b:
                res += 1
                b -= 1

        #after iterating through all letters, return the total amount of letters that need to be deleted
        return res
