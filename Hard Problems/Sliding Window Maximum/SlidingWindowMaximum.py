class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #store indices in the monotonic queue based on the num list values
        #before adding a new element, remove all indexes whose values are smaller than the current one
        #remove the leftmost index if it is outside the range of the current window
        #once the window reaches k length, append the the current maximum, found through the front of the deque, to the result list
        #return the list of max values when the left and right pointers are k apart and the right pointer reaches the end of the list

        res = []
        q = deque() 

        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1 

        return res