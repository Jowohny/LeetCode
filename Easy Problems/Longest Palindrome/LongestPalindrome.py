class Solution:
    def longestPalindrome(self, s: str) -> int:

        #create a frequency list out off all the letters in the given string
        freq  = collections.Counter(s)

        #use this to keep tracking of the length of the longest possible palindrome
        longest = 0

        #if there are any odd frequecies, take note of it through this boolean
        odd = False

        #go through every letter in the frequency list
        for l in freq:

            #if the frequency of the current letter is even, then we can just add it to the length since even frequencies can split cleanly
            #if the frequency of the current letter is odd, then change the value of the odd boolean to be true and add the frequency minus one to make it even
            if freq[l]%2==0:
                longest += freq[l]
            else:
                odd = True
                longest += freq[l]-1

        #if throughout the loop, we found that a letter had an odd frequency, then add another one length to the longest frequency we can make
        #in terms of even length palindromes, this won't matter as much, but in odd length palindromes, this plus one will account for one of the letters we took away before adding them to the length of the longest frequency, since one letter can be stuck directly in the middle
        if odd:
            longest += 1
        
        #after all frequencies and characters have been accounted for, return the length of the longest possible palindrome
        return longest

