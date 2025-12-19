class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        #final list to deposit popped values into
        res = []

        #initialize the heap using the game array
        heapq.heapify(nums)

        #we continue the game until there are no values left in the heap
        while len(nums) > 0:
            
            #in each turn, alice gets the current smallest number, then bob gets the next smallest number
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums) if nums else None
        
            #if bob has a valid value in his turn, then add bob's value to the resulting list before alice's
            if bob != None:
                res.append(bob)

            res.append(alice)
        
        #return the resulting array after the game is complete
        return res
