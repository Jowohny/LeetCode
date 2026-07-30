class Solution:
    def minimumPushes(self, word: str) -> int:
        #there are 8 usable keys, each key can hold multiple letters stacked on top of each other
        #the first letter on a key costs 1 push, the second costs 2, the third costs 3, and so on
        #the letters we type most often should get the cheapest slots to keep the total pushes down
        #count how often each letter appears, then sort those counts from most frequent to least
        #hand out the 8 cheapest slots first, the next 8 letters cost 2 each, the next 8 cost 3, etc

        count = [0] * 26

        #tally how many times each letter shows up in the word
        for ch in word:
            count[ord(ch) - ord('a')] += 1

        #line the letters up from most frequent to least frequent
        count.sort(reverse=True)

        res = 0

        #the ith most frequent letter sits at push cost (i // 8) + 1
        for i in range(26):

            #once we hit letters that never appear, theres nothing left to add
            if count[i] == 0:
                break

            res += count[i] * (i // 8 + 1)

        return res
