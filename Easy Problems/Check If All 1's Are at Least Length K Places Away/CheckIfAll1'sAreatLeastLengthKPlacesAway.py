class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        #keep a couple variables to keep track of the distance between ones and another to know if we have beginning 1 to base the distance off of
        #when we find a 1, we make it so we know we found 1
        #for every item that is 0, we add 1 to the distance
        #in the case that we find another 1, we initially check if another 1 has already been found and whether the current distance is greater than the given k
        #if the distance is found to be less than the k, return false
        #otherwise set the current distance to 0 restart the count of the distance
        #after visiting each item in the array, return true if the values in the array didnt return false

        distance1 = 0
        current1 = False
        for i in nums:
            if i == 1:
                if distance1 <= k and current1:
                    return False
                distance1 = 0
                current1 = True
            distance1 += 1
        
        return True
            