
class Solution:
    def reverseVowels(self, s: str) -> str:
        #define what all the values are
        vowels = {'a':1, 'e':1, 'i':1, 'o':1,'u':1}

        #turn immutable string into list for faster run time
        res = [l for l in s]

        #create 2 pointers to pick up vowels
        l,r = 0,len(s)-1

        #loop until the pointers overlap
        while l < r:

            #if the current letter isn't a vowel, the value with be 0, if it is a vowel, the value will be 1 defined by the dictionary
            vc1 = vowels.get(s[l].lower(),0)
            vc2 = vowels.get(s[r].lower(),0)

            #if the current letter isn't a vowel, then move the pointer accordingly
            if not vc1:
                l += 1
            if not vc2:
                r -= 1

            #if we have picked up both vowels on each side, swap them and increment and decrement accordingly
            if vc1 and vc2:
                res[l],res[r] = res[r],res[l]
                r -= 1
                l += 1

        #combine the list elements back into one string
        return ''.join(res)

