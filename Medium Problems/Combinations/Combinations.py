class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        #create a backtracking method that starts from a number 'id', keeps track of how many numbers we picked, and stores the current combination
        def backtrack(id, combo):

            #if we picked a total of k numbers, add a copy to the result list
            if len(combo) == k:
                res.append(combo.copy())
                return

            #go through all numbers from id to n as to not run over the same number or combination variation again
            for i in range(id, n+1):

                #add number to the current combination, keep going with the next number, and then remove after testing
                combo.append(i)
                backtrack(i+1, combo)
                combo.pop()
        
        #result list and starting call
        res = []
        backtrack(1, [])

        #return all combinations
        return res
