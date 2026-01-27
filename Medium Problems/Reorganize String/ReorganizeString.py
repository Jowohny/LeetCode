class Solution:
    def reorganizeString(self, s: str) -> str:

        #use an array to store all the letters to recombine later so we don't have to reconstruct an immutable string
        res = []

        #create a frequency list of all the letters in the string
        freq = collections.Counter(s)

        #store all the letters and their frequencies in an array, inverting the frequency to effectively create a max heap
        lList = [(-f,l) for l,f in freq.items()]
        heapq.heapify(lList)

        #loop until all letters are used or we find out that we are unable to create a reorganized string
        while lList:

            #pop the item with the most frequent letters and unpack it
            count1, l1 = heapq.heappop(lList)

            #if the last letter in the final string array is the same as the one that is currently popped off, then pop off the next most frequent letter
            if res and res[-1] == l1:

                #if there is nothing else to pop off, then we are unable to create a properly reorganized string
                if not lList:
                    return ""

                #popping off the next most frequent letter in the heap
                count2, l2 = heapq.heappop(lList)
                
                #add that letter to the final string array and decrease the count of that letter
                res.append(l2)
                count2 += 1
                
                #if there are 0 remaining, then add them back into the heap
                if count2 < 0:
                    heapq.heappush(lList, (count2, l2))

                #since we didn't use any of the original letters that we popped in the beginning, put them back into the heap as they were
                heapq.heappush(lList, (count1, l1))

            #this case means that the last the current letter popped is not the same as the last letter in the final string array
            else:

                #add the current letter into the final string array and decrease its count
                res.append(l1)
                count1 += 1
                
                #if there are more than 0 of that letter remaining, add it back into the heap
                if count1 < 0:
                    heapq.heappush(lList, (count1, l1))

        #after all is done, join all the letters in the array into one string and return it
        return ''.join(res)