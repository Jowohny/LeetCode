class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        #initialize a deque with the starting index
        q = deque([start])

        #use a set make sure we don't visit the same indexes later
        visited = set()

        #loop until we have processed all reachable indexes
        while q:

            #pop the deque to process the next index
            curr = q.popleft()

            #if the current index's value is 0, then return true
            if arr[curr] == 0:
                return True

            #if we jump the current index value spaces forwards from the current index and its in bounds of the list, then add it to the queue for later processing and add it to the visited set so we don't revisit it later
            if 0 <= curr + arr[curr] < len(arr) and curr + arr[curr] not in visited:
                q.append(curr + arr[curr])
                visited.add(curr + arr[curr])

            #if we jump the current index value spaces backwards from the current index and its in bounds of the list, then add it to the queue for later processing and add it to the visited set so we don't revisit it later
            if 0 <= curr - arr[curr] < len(arr) and curr - arr[curr] not in visited:
                q.append(curr - arr[curr])
                visited.add(curr - arr[curr])

        #after processing all the reachable index without finding 0, return False as it is not possible to reach 0 with the giving starting index
        return False
