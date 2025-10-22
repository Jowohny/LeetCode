class Solution:
    def merge(self, nums1, m, nums2, n):
        #we start from the end of both lists since nums1 has empty spots at the back
        #while both lists still have numbers left, we compare the end values
        #whichever is bigger gets placed at the end of nums1, we move that pointer back one step and keep going
        #when nums2 still has leftovers, we place them at the end of nums1 since leftovers will be greater than all the elements in nums1
        #in the end nums1 will be fully sorted with all numbers merged in order
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
