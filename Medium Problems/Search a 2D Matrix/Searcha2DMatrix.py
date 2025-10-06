class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search
        #use pointers to keep dividing the list in half so it runs at log n
        #at every midpoint, check if its on target, if not, resort to moving either
        #left or right pointer depending on if the target is less than or greater than
        #current value at the midpoint

        nt = (len(matrix)*len(matrix[0]))-1
        l,r = 0,nt

        while l <= r:
            m = (l+r)//2
            grid = matrix[m//len(matrix[0])][m%len(matrix[0])]

            if grid == target:
                return True
            elif grid < target:
                l = m+1
            else:
                r = m-1
        return False