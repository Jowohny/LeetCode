# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #use 2 pointers set to either sides of the range from 1 to n
        #find the middle of the range and check whether it is bad or not
        #if not then move the left pointer 1 to the right of the middle, otherwise move the right pointer to the middle
        #after the pointers overlap, return the index of the left pointer
        l,r = 0,n
        while l < r:
            m =  (l+r)//2
            if not isBadVersion(m):
                l = m+1
            else:
                r = m
        return l