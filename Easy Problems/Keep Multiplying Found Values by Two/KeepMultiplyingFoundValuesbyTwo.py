class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
				#create a dictionary to add in values that aren't equal to the orginal or any multiples
				#if the current number in the list is equal to the original, then multiply by 2
				#check in the dictionary to see if the current original value is in there, if it is there multiply by 2 and repeat until there are no more
				#if the current number is not equal to the original, then add it to the dictionary
				#we used a dictionary to lookup other numbers we found before in O(1) time
        numList = defaultdict(int)
        for i in nums:
            if i == original:
                original *= 2
                while  numList[original] == 1:
                    original *= 2
            else:
                if numList[i] == 0:
                    numList[i] = 1
        return original

    

    