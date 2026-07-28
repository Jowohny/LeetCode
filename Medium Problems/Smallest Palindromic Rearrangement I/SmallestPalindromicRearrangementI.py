class Solution:
    def smallestPalindrome(self, s: str) -> str:
        #the string is already a palindrome, so every character count is even except maybe one middle character
        #to make the smallest palindrome, only half the characters actually matter, the other half is just a mirror
        #count every character, then take half of each count to build the first half
        #lay those halves down in sorted order so the front of the string is as small as possible
        #the odd character out (if any) sits in the middle, then mirror the first half to close the palindrome

        count = [0] * 26

        #tally how many times each letter shows up
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        firstHalf = []
        middle = ''

        #walk the letters in alphabetical order so the smallest ones land at the front
        for i in range(26):
            ch = chr(i + ord('a'))

            #half of each letter goes into the first half, the mirror covers the other half
            firstHalf.append(ch * (count[i] // 2))

            #a letter with an odd count is the single middle character of the palindrome
            if count[i] % 2 == 1:
                middle = ch

        firstHalf = ''.join(firstHalf)

        #mirror the first half onto the end to close out the palindrome
        return firstHalf + middle + firstHalf[::-1]
