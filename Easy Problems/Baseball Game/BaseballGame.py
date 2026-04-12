class Solution:
    def calPoints(self, operations: List[str]) -> int:

        #create an array to keep all the game points in
        game = []

        #loop though every point or operation in the game
        for o in operations:

            #if the operation is a '+', add the 2 previous scores, append it to the game list, and skip everything else
            if o == '+':  
                game.append(game[-1] + game[-2])
                continue

            #if the operation is a 'D', then double the last score, add it to the game list, and skip everything else
            if o == 'D': 
                game.append(2*game[-1])
                continue

            #if the operation is 'C', then pop off the latest score in the game list and skip everything else
            if o == 'C':
                game.pop()
                continue
            
            #if everything else has passed, then the current operation is a number, so convert it and add it to the game list
            game.append(int(o))

        #use this to keep track of the points
        points = 0

        #after the game is finished, add together all the points
        for n in game:
            points += n

        #return the total amount of points
        return points

            
