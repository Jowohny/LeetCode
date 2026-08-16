class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #rotating right by k just moves the last k numbers to the front and pushes everything else back
        #k can be bigger than the array, so wrap it with a mod so we only rotate as much as we actually need
        #the trick is to reverse the whole array first, which flips everything backwards
        #then reverse just the first k numbers, and reverse the rest after them, and everything lands in the right spot
        #do it all in place with a two pointer helper so we dont need a second array

        n = len(nums)

        #trim k down so we arent doing full extra loops around the array
        k %= n

        #helper that reverses the chunk between the left and right indices in place
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        #flip the entire array, then fix the two pieces back into forward order
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
