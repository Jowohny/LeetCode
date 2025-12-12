class Solution(object):
    def twoSum(self, nums, target):
        #create a hashmap
        #enumerate values of num list to create indexed values
        #find the difference between current value and target
        #try to find the different as a key within the hashmap
        #if found then return key value pair, if not then add to current hashmap
        hashmap = {}

        for i,v in enumerate(nums):
            difference = target-v

            if difference in hashmap:
                return [i, hashmap[difference]]
            hashmap[v] = i 

        