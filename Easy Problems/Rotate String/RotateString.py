class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        #if the length of each of the strings aren't equal, then they can't be rotations of each other
        if len(s) == len(goal):

            #when concatinating the same string together, somewhere along the string, it has a rotation of itself in there
            #goal is only a rotation of s if goal in found in the within the string of s+s
            if goal in s+s:
                return True
            else:
                return False
        else:
            return False