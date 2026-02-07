class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        #keep a global max value as we travel through the sentence
        currMax = float('-inf')

        #split the sentence up by the spaces in the sentence
        #iterate through the list of 'words' created by the split
        for c in s.split(' '):

            #if the current item in the list isn't a number, then skip it
            if not c.isdecimal():
                continue
        
            #if the current item is a number, then convert it to an integer and compare it to our global max
            #if it happens to be greater than the max, set the current number as the new max
            #if it is less than or equal to, that means the numbers found so far aren't ascending, so return false
            if int(c) > currMax:
                currMax = int(c)
            else:
                return False

        #if we get through all the words, that means either there were no numbers or all numbers found were in ascending order
        return True