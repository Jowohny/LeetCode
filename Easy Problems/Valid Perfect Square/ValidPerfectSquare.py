class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #initialize 2 pointers, both of them at either side of the range from 1 to num
        #check the middle to see if its square is higher or lower the number
        #if the middle times itself is higher, then set the left pointer 1 to the right of the middle
        #if it is lower, then set the right pointer 1 to the left of the middle
        #if it is equal then return True
        #if the pointers overlap and we haven't found a perfect square, then return False
        l,r = 0,num
        while l <= r:
            m = (l+r)//2
            if m*m == num:
                return True
            if m*m < num:
                l = m+1
            else:
                r = m-1
        return False