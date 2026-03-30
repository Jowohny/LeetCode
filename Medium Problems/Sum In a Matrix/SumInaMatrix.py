class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        #sort all sublists within the matrix
        nums = [sorted(m) for m in nums]

        #keep a score count
        score = 0

        #for each round of taking out the max number from each matrix, keep a list to compare them
        curr = []

        #only loop for the number of elements in each sublist
        for _ in range(len(nums[0])):

            #for every sublist within the matrix, pop the last item off, which is the largest element since we sorted
            #add that item to the max element list
            for m in nums:
                curr.append(m.pop())

            #compare all the max values from each sublist and add the greatest one to the score
            score += max(curr)

            #reset the list for the next round of comparison
            curr = []
        
        #return the total score after all elements are processed
        return score