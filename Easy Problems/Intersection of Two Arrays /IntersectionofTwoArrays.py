class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
				#turn both nums lists into a set to get rid of duplicates
				#use & operator or find the intersection (the numbers in which both lists have)
				#convert to list as set come in {} and not []

        return list(set(nums1) & set(nums2))
        