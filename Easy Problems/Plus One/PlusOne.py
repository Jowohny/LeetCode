class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #grab the last value in the list and add one to it
        #if the last digit is 9, carry over the one
        #if all numbers in list are 9, return a new list of 
        #of the length of digits + 1 and set the first index
        #to 1 and the rest to 0

        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(i,1)
        return digits