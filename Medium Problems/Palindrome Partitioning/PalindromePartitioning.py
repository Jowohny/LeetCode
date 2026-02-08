class Solution:
    def partition(self, s: str) -> List[List[str]]:\
    
        #stores all the different partitions
        res = []

        #changes as we explore the different combinations of the given string
        palinPart = []

        #method use to determine whether the given substring is a palindrome
        def isPalindrome(part):

            #define 2 pointers at each end of the substring
            l,r = 0,len(part)-1

            #loop until the pointers start to overlap
            while l < r:

                #if at any point the characters aren't equal, then the substring isn't a palindrome
                if part[l] != part[r]:
                    return False

                #bring the pointers one step closer to each other
                l +=1 
                r -= 1

            #after all the letters match all the way through, then the substring is a palindrome
            return True

        #backtracking method used to find different combinations of the same string
        def backtrack(i):

            #if the current index is out of bounds, then we have a valid partition, so we add a copy of the current variation to the final list
            if i >= len(s):
                res.append(palinPart[:])
                return

            #loop through the remaining letters given by the index to start
            for j in range(i, len(s)):

                #if the current substring is a palindrome, add it to the current combination list
                if isPalindrome(s[i:j+1]):
                    palinPart.append(s[i:j+1])

                    #call the method again using the loop index so we can find other valid substrings beyond this index
                    backtrack(j+1)

                    #after going down one path, pop off the last item in the list of palindromes to allow other combinations to be tested
                    palinPart.pop()

        #initial call to the backtracking method starting at the 0th index
        backtrack(0)

        #after all combinations of substrings have been tested, return all the valid partitioned palidromes
        return res