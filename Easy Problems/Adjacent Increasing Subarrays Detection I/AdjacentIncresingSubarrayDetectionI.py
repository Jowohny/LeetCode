class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        #define a helper function to check whether a subarray of size k is strictly increasing  
        #loop through the subarray from the starting index to the k-1 index  
        #at each step, compare the current number with the next number  
        #if any number is greater than or equal to the next, return False since it breaks the increasing rule  
        #if the whole loop passes without returning False, return True since the subarray is strictly increasing  

        #loop through the list to find pairs of adjacent subarrays of size k  
        #stop early so both subarrays of size k can fit in the array  
        #at each index, call the helper function on the current subarray and the next adjacent subarray (start at i + k)  
        #if both are strictly increasing, return True since we found the required adjacent subarrays  
        #if no such pair is found by the end of the loop, return False  

        
        def increasing(i):
            for i in range(i, i + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            
            return True

        
        for i in range(len(nums)- k - k + 1):
            if increasing(i) and increasing(i + k):
                return True
        
        return False