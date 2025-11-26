class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #we add a 0 to the end of the list to represent the place we need to get to, aka the top of the stairs
        #iterate backwards from the end of the list so we can bring the total cost to the beginning
        #from the current step, take the minimum cost from either the next step or the step after that
        #by taking the minimum cost at each step, we can see the path of least resistance to get us to that end index of 0 we added
        #after we have reached the beginning of the list, compare the first 2 elements as we are allowed to start at either the first or the second step
        #return the element with the lower cost as it represents the least cost way to reach the top
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])