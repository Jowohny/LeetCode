class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #create a fast and slower pointer
        #use an initial loop to find an intersection
        #break out the loop when the fast and slow pointer meet
        #keep the fast pointer at the intersection point and reset slow pointer back to first index
        #run a loop increments the slow pointer until the it matches at the intersection confirming the duplicate
        slow,fast = nums[0],nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        