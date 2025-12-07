class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #[3,7] 5 3,5,7 in between
        #[4,8] 5 5,7 in betweem
        #[4,7] 4 5,7 in between
        #[3,6] 4 3,5 in between

        #of all different variations, the only difference i noticed was that that interval with both odds as the high and low have 
        #a higher have an additional non negative count after flooring the difference between high and low
        if low%2==1 and high%2==1:
            return math.ceil((high-low)/2)+1

        return math.ceil((high-low)/2)