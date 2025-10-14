class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        #grab the values from the first and last items in the list
        #swap both of them and use the loop to gradually go in from one side till it reaches the middle
        
        for i in range(len(s)//2):
            s[i],s[-(i+1)] = s[-(i+1)],s[i]