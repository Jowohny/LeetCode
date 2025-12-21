class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #make a set to store all the seen through the process
        seen = set()

        #loop through every number within the array
        for n in arr:

            #if the current numbers double exists in the set the return true
            #if the current number is even and its half is found in the set, also return true
            if n*2 in seen or (n%2==0 and n//2 in seen):
                return True
            
            #if the current number's half or double isn't found in the set, then add the current number
            seen.add(n)

        #after going through all numbers in the array, if no doubles or halfs where found in the process, return false
        return False
