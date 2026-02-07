class Solution:
    def checkString(self, s: str) -> bool:
        
        #use this to keep our index along the string
        i = 0

        #only loop while the index is within bounds
        #for the first run, loop while the current letter is 'a'
        while i < len(s) and s[i] == 'a':

            #increment the index so we can process the next letter
            i += 1
            
            #if we have reached the end of the string, then that means that the entire string was made of a's, so technically there are no b's for the a's to come before, so return true
            if i == len(s):
                return True

        #only loop while the index is within bounds
        #for the second run, loop while the current letter is 'b'
        while i < len(s) and s[i] == 'b':

            #increment the index so we can process the next letter
            i += 1

            #if the current index is within bounds at any point during this loop we run across an 'a' then all a's didn't come before all b's, so return false
            if i < len(s) and s[i] == 'a':
                return False

        #if we have reached the final index, that means all the a's have come before the b's, so return true
        return True