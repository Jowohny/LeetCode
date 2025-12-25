class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        #sort the list so we have all the happiest children on top of the list
        happiness.sort()

        #keep a total count to know how much happiness we get from k children
        total = 0

        #loop k times to get the happiness from k amount of kids
        for i in range(k):

            #pop the child from the list with the most happiness, take away one point of happiness for each child already taken
            curr = happiness.pop() - i

            #if the current child's happiness is still above 0, then add it to the total, otherwise break out the loop
            if curr > 0:
                total += curr
            else:
                break

        #return the total amount of happiness
        return total