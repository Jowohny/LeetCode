class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #convert the string into a lists since string are immutable
        #define a reverse function to reverse the lists at a certain substring
        #iterate twice the k to in order to do every other substring of k
        #when defining the right index in the function, make sure to call the minimum between the length of the list and the index to keep the right index within the bounds, also to make sure to still swap items just in case the next k substring doesnt get cut off

        s = list(s)

        def reverse(l: int, r: int) -> None:
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        
        for i in range(0, len(s), 2 * k):
            reverse(i, min(i + k - 1, len(s) - 1)) 

        return ''.join(s)
