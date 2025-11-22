class Solution:
    def countHomogenous(self, s: str) -> int:
        #have a counter to count the amount of consecutive letters, one to incrememnt the total about of homogenous substrings, and another to keep track of the current letter so we know which letter is consecutive
        #if we see that the current letter in the string is the same as the current letter stored, increment the consecutive count and add it to the total
        #if its not, reset the consecutive count, change the stored letter to the current letter and add 1 to the total as it represents the beginning of a possible homogenous substring
        #return the total amount of homogenous substrings after the entire string is processed
        
        count = 0
        current = s[0]
        total = 0

        for i in s:
            if i == current:
                count += 1
                total += count
            else:
                current = i
                count = 1
                total += count
        return total % ((10**9) + 7)