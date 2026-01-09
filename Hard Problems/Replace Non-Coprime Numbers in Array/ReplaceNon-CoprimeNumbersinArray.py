class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        #use a stack to add values and remove values into as we go operate on each number in the nums list
        res = []

        #iterate through each number in the nums array
        for n in nums:

            #add the current number into the result array to be processed later
            res.append(n)

            #only perform operations if there are more than 2 items in the stack
            while len(res) > 1:

                #a number is non coprime if its greatest common denominator is greater than 1
                if math.gcd(res[-1],res[-2]) > 1:

                    #get the top 2 items on the stack
                    n1,n2 = res.pop(),res.pop()

                    #a math trick to find the lowest common fact is the mulltiply the numbers and divide them by their greatest common factor
                    res.append(n1*n2 // math.gcd(n1,n2))
                else:

                    #if the numbers are coprime then stop operations
                    break

        #return the result after all number in the resulting list aren't non coprime linear next to eachother
        return res
                
                    