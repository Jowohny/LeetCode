class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create a list of pairs that combine each car's position and speed together
        #sort the pairs in reverse order based on position so we start from the car closest to the target
        #initialize an empty stack to keep track of the time each car takes to reach the target
        #iterate through each pair of position and speed in reverse sorted order
        #for each car, calculate the time it takes to reach the target using (target - position) / speed
        #append that time to the stack
        #check if the current car's time is less than or equal to the car before it in the stack
        #if so, it means they form a fleet since the current car will catch up to or arrive at the same time as the previous one
        #in that case, pop the current time from the stack to merge them into one fleet
        #after going through all cars, the number of fleets is equal to the remaining number of items in the stack


        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair: 
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)