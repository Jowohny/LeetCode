class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #create a whole list, initializing it with False to represent the indexes where words haven't been found from the word dictionary to fit in that specific place
        #make the cache one element longer than the string to act as the base case
        cache = [False] * (len(s)+1)

        #set the last element of the cache equal to True
        cache[len(s)] = True


        #start from the end of the string and work backwards to build words
        for i in range(len(s)-1, -1 ,-1):

            #at every index, check every word in the dictionary so see if theres a match
            for w in wordDict:

                #only change the cached values if the length of the current word from the dictionary put on top of the current index is within the bounds of the string itself
                #if the current word is within bounds for the current string, splice the string and check if the substring is equal to the current word
                #change the current index cache to what is found at the end of the current word in relation to the current index
                #it represents that a the current index can be chained to the next word represented as True within the cache
                if (i + len(w)) <= len(s) and s[i: i+len(w)] == w:
                    cache[i] = cache[i+len(w)]

                #if we have already found a word at this that fits the requirements, there is no need to continue searching for it, so break out of the current loop
                if cache[i]:
                    break

        #return the 0th value of the cache, if it is True, then there was a path of words from the dictionary to connect the beginning to the end, meaning that all the words were broken up from the string successfully
        return cache[0]