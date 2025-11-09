class BrowserHistory:
    #initialize 2 stacks one for the forward history and the other for the back history and add the homepage to the initial back stack 
    #when visiting a site, all sites stacked in the forward history gets removed and the current url gets added to the back stack
    #when moving backwards, we pop from the back history stack and add that to the front history stack for later access
    #something else to note is so make sure there the back stack doesn't go lower than 1 in length
    #when moving forwards, we pop from the forward history stack and add that to the back history stack
    #after going forwards or backwards, return the top of the back history stack as that represents our current place in the browser

    def __init__(self, homepage: str):
        self.backHistory = [homepage]
        self.frontHistory = []
        

    def visit(self, url: str) -> None:
        self.frontHistory.clear()
        self.backHistory.append(url)
        

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.backHistory) > 1:
            if self.backHistory:
                self.frontHistory.append(self.backHistory.pop())
            steps -= 1
        return self.backHistory[-1]


    def forward(self, steps: int) -> str:
        while steps > 0 and self.frontHistory:
            if self.frontHistory:
                self.backHistory.append(self.frontHistory.pop())
            steps -= 1
        return self.backHistory[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

#stack[visit1,visit2,visit3]
#stack[]