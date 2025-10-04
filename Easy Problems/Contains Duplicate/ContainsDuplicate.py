class Solution(object):
    def containsDuplicate(self, nums):
			#use sets to rid of any duplicates
			#if set with nums has less numbers than the original, then nums list contains duplicate

			if len(set(nums)) == len(nums): 
					return False
			else:
					return True