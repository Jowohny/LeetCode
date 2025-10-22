class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #very easy solution, maybe a little bit too easy, definitely an optimized version better than this though
        #just sort the numbers so they are in ascending order 
        #use negative index to grab k amount from the end of the list
        nums.sort()
        return nums[-k]