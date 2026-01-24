class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        #create a frequency list using all the numbers in the list
        freq = collections.Counter(nums)

        #create another list only keeping the frequency of the numbers that are even
        evenFreq = [(-f,n) for n,f in freq.items() if n%2==0]
        
        #if there are no even numbers, then there can't be a most frequent even number, return -1
        if len(evenFreq) == 0:
            return -1

        #by adding the frequency as a negative, we pretty much have an inversed list where the most frequent element is first
        #if there are multiple elements that are the most frequent, then the number itself will be sorted
        #the frequency will be sorted by the max element while the number is sorted by the min element
        evenFreq.sort()

        #return the first element found in the list
        return evenFreq[0][1]