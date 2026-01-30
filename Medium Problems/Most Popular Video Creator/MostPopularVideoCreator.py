class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        #create an array to store the most viewed videos from the most popular creators
        res = []

        #create a sort of nested dictionary using a lambda to store each creaters total view count, most viewed video and its id
        stats = collections.defaultdict(lambda: {"t": 0, "bV": -1, "bI": ""})

        #keep track of the most views held by any creator
        mostViews = 0
        
        #loop through a zipped list of creators, ids, and video views so we can keep the videos and other information to their respective creators
        for c, i, v in zip(creators, ids, views):

            #get the information of the current creator
            currCreatorInfo = stats[c]

            #add the views of the current video to the current creators current view count
            currCreatorInfo["t"] += v
            
            #if the total view count of this creator passes to global max, update the global max
            if stats[c]["t"] > mostViews:
                mostViews = stats[c]["t"]
            
            #if the views of the current video passes the creators recorded most viewed video, then update the creator's best video and its id
            #if the views of the video matches the creators best recorded one, then update the creator's best video and id if the current video's id is lexographically smaller than the current recorded id
            if (v > currCreatorInfo["bV"] or 
                    (v == currCreatorInfo["bV"] and 
                        (currCreatorInfo["bI"] == "" or i < currCreatorInfo["bI"]))):
                currCreatorInfo["bV"] = v
                currCreatorInfo["bI"] = i
        
        #after filling in all the information into the stats, loop through each item in the dictionary 
        for c, data in stats.items():

            #if the current creator matches the count of the most views recorded globally, then add them to the final result with their most viewed video
            #we keep a global max in the case where multiple creators have equally the most views
            if data["t"] == mostViews:
                res.append([c, data["bI"]])
                
        #return the list of creators and their video that has the most views
        return res