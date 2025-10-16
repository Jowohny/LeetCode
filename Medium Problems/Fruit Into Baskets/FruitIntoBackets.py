from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #we use a sliding window to keep track of a range of trees
        #traverse the list using the right pointer, counting how many of each fruit type we have along the way
        #if we have more than 2 types at any point, we increment the left side of the window up until we’re back to 2
        #decrement the amount of fruits found in the current window and remove the type of fruit when there are no more of them
        #compare the length at each iteration to find the max length window overall
        #at the end we return the length of the biggest window we found

        trees = 0
        currFruits = defaultdict(int)

        l = 0 
        for r in range(len(fruits)):
            currFruits[fruits[r]] += 1

            while len(currFruits) > 2:
                currFruits[fruits[l]] -= 1
                if currFruits[fruits[l]] == 0:
                    del currFruits[fruits[l]]
                l+=1

            trees = max(trees, r-l+1)
        return trees

            
            
                
            