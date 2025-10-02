class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #create a temp variable where we store a sorted list
        #create a dictonary to store index positions and value pairs
        #iterate through the sorted list and add each of them to the dictionary with its index
        #the index indicates how many number are smaller it it shows how many numbers come before it
        #create another list and go through all dict values

        temp = sorted((nums))
        d = {}
 
        for index, value in enumerate(temp):
            if value not in d:
                d[value] = index
        res = []
        for i in nums:
            res.append(d[i])
        return res
