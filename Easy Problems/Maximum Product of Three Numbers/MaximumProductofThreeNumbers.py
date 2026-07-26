class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #the biggest product is either the three largest numbers multiplied together
        #or the two smallest numbers (which could be big negatives) times the single largest number
        #two negatives multiply into a positive, so that pair can beat the top three
        #track the three largest and two smallest values in one pass
        #compare both candidate products and return the greater one

        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for n in nums:

            #slot the current number into the running top three largest
            if n >= max1:
                max1, max2, max3 = n, max1, max2
            elif n >= max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n

            #slot the current number into the running two smallest
            if n <= min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n

        return max(max1 * max2 * max3, min1 * min2 * max1)
