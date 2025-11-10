class Solution:
    def isHappy(self, n: int) -> bool:
        #create a set for the purpose of letting us know when we've already encountered a number
        #we continue operations until we reach a false state or our current number is 1
        #for every run, we pop the each digit of the number until it reaches 0, square each of them and add them together
        #if its not equal to one and the current number isnt in our set, then we add it to the set and continue
        #if its already in the set, then that we encountered a loop and it will never a happy number
        #if the total comes out to be 1 for the current round, then return true as that means its a happy number
        nonHappy = set()
        while n != 1:
            curr = 0
            while n > 0:
                oD = n % 10
                n //= 10
                curr += oD**2  
            if curr == 1:
                return True 
            if curr not in nonHappy:
                nonHappy.add(curr)
            else:
                return False
            n = curr
        return True