class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #we want two equal numbers whose indices are at most k apart
        #keep a dictionary that remembers the most recent index each number was seen at
        #as we walk the array, check if this number showed up before and how far back it was
        #if the gap between now and that last index is k or less, we found our pair
        #otherwise update the number's latest index and keep going

        seen = {}

        for i, n in enumerate(nums):

            #if we saw this number recently enough, the two indices are within k
            if n in seen and i - seen[n] <= k:
                return True

            #remember the latest index this number appeared at
            seen[n] = i

        return False
