class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #the range will be the max number within the largest number in the array
        #use binary search to find the minimum amount of bananas need to eat per hour
        #the amount of bananas is calculated by the current rate of bananas eaten 
        #going through the list using ceiling operation on each value

        l,r = 1,max(piles)
        lesser = r

        while l <= r:
            m = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/m)
            if hours > h:
                l = m + 1
            else:
                lesser = m
                r = m - 1
        return lesser