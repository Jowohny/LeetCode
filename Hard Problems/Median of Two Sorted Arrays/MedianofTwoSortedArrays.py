#probably not the best solution for this but it works lol, time complexity is kinda wack tho

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #add both arrays to make another array that has all elements from nums1 and nums2
        #sort the array to make it easier to find the index
        #if the length of the new list is odd, divide the length of the list by 2 to find the middle index
        #if the length of the new list is even, find the 2 middle most indexes and take the average
        #return the median

        newArray = nums1 + nums2 
        newArray.sort()
        n = len(newArray)

        if len(newArray) % 2 == 1:
            return newArray[n//2]
        else:
            return ( newArray[n//2] + newArray[(n//2)-1] ) / 2