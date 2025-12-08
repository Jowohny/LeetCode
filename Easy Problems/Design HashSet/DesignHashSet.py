class MyHashSet:

    def __init__(self):
        #create a set
        self.hash = set()

    def add(self, key: int) -> None:
        #use .add to add key into set
        self.hash.add(key)
        

    def remove(self, key: int) -> None:
        #check if the key is in the set and if it is in set
        if key in self.hash:
            self.hash.remove(key)

    def contains(self, key: int) -> bool:
        #check if the key is in the hash, return true if it is in the set, return false otherwise
        if key in self.hash:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)