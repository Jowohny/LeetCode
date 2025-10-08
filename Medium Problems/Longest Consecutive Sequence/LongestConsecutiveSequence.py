class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #put all num list in a set to remove all duplicates
        #use a variable to keep track of longest consecutive sequence
        #use a for loop to run through all numbers in the set
        #check at each number if there is a value that is one less than the current
        #if there is such a number, increment the length of the longest by 1
        #in a while loop, check how many number in succession in the current set
        #return the the length of the longest consecutive set after for loop completion

        setN = set(nums)
        longest = 0

        for num in setN:
            if num-1 not in setN:
                length = 1
                while num+length in setN:
                    length += 1
                longest = max(longest, length)
        return longest