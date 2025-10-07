class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #convert the number into a string
        #compare edge values to see if they are the same
        #if found to be false part way through, return false
        #if it gets through the whole loop then return true

        rep = str(x)

        for i in range(len(rep)//2):
            if rep[i] != rep[len(rep)-i-1]:
                return False
        
        return True