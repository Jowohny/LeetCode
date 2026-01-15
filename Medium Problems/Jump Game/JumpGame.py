class Solution:
    def canJump(self, nums: List[int]) -> bool:

        #start the goal post at the end of the list
        goal = len(nums)-1

        #iterate through the list backwards
        for i in range(len(nums)-1, -1, -1):

            #if we are able to jump to the current goal post from the current index, move the goal post back to that index
            if i + nums[i] >= goal:
                goal = i

        #if we have successfully moved the goal post back all the way to 0, then it is possible to reach the last index
        return False if goal != 0 else True