class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #create a counter for all the different tasks that need to be processed
        #convert the dictionary to a list and convert at all the values to negative to effectively create a max heap
        #create another variable to keep a track of the current time
        #if there exists anything in the heap, pop it, and add to the queue with its frequency and the next available time it can be use if there are more than 0 instances of it
        #if there is anything left in the queue and the time matches the next available item from the queue then push it onto the stack
        #after there are no more tasks in the heap and queue, return the time
        freq = Counter(tasks)
        maxHeap = [-f for f in freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count:
                    q.append([count, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time