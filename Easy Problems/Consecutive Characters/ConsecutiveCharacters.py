class Solution:
    def maxPower(self, s: str) -> int:
        #have a counter to keep track of the current amount of consecutive letters for the current letter, another variable to keep track of the most consecutive letters, and another to dynamically change as we count the different letters
        #if the current letter in the string is the same as the stored letter, incrememnt the current consecutive counter
        #otherwise take the max between the most consecutive and the current consecutive count, reset the count, and then change the stored letter for the future consecutive letters
        current = s[0]
        mostC = 1
        currentC = 1

        for i in s[1:]:
            if current == i:
                currentC += 1
            else:
                mostC = max(mostC, currentC)
                current = i
                currentC = 1

        return max(mostC, currentC)
