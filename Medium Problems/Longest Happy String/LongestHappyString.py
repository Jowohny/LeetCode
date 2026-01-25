class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

				#use a list or create the string, strings are immutable so we'd have to create a new string every time something is added
        #store counts as negative values will give us max heap instead of min heap
				#only store letters in the heap only if they have more than 0 usable letters
        res = []
				letterHeap = []
        for count, c in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(letterHeap, (-count, c))

				#loop until all the either all letters are consumed or the until the string condition can't be met
        while letterHeap:

            #pop the character with the highest remaining letters left
            count1, c1 = heapq.heappop(letterHeap)

            #check if using this character would create three in a row
            if len(res) >= 2 and res[-1] == res[-2] == c1:

                #if there are no other characters available, we can't continue building the string
                if not letterHeap:
                    break 

                #use the second most frequent character instead to break the pattern and decrease how much it has remaining
                count2, c2 = heapq.heappop(letterHeap)
                res.append(c2)
                count2 += 1 

                #if this character has more letters to be used, push it back into the heap
                if count2 < 0:
                    heapq.heappush(letterHeap, (count2, c2))

                #push the first character back into the heap since we didn't use it
                heapq.heappush(letterHeap, (count1, c1))
            else:

                #given the first if condition, this character is safe to add to the result and decrease the amount remaining
                res.append(c1)
                count1 += 1

                #if this character has more letters to be used, push it back into the heap
                if count1 < 0:
                    heapq.heappush(letterHeap, (count1, c1))

        #combine all characters into a string and return
        return ''.join(res)

