class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        #keep a variable to bitshift and add bits to know our value within the array and another to put in the result of each number
        #go through every value in the nums list, before adding each bit to the current number, we left shift the bit values which add a 0 all the way to the right of the bit value
        #after bit shifting, we add the current bit in the list to the 0 that got shifted in
        #we check each number after the operations and add true or false to the result list depending on if the number is divisible by 5
        #after we get through all in the list, return the list of trues and falses
        currNum = 0
        res = []
        for n in nums:
            currNum = (currNum << 1) + n 
            res.append(currNum % 5 == 0)
         
        return res