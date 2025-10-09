class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # initialize our doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # return the value of a key if it exists
        # if the key doesn't exist in cache
        # then return -1
        # when we use the get operation, this item becomes the most recently used
        # so we need to push it to the end of the list
        # using an add method
        # then we return the value of the node we just added to the end
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # remove first, then add
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # if the key exists:
        # 1. move that node to the end of the list (most recently used)
        # 2. check if the addition of the node exceeds capacity
        # if so, we remove the node at the head.next value
        if key in self.cache:
            oldNode = self.cache[key]
            self.remove(oldNode)
        
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            nodeDelete = self.head.next
            self.remove(nodeDelete)
            del self.cache[nodeDelete.key]
            
    
    def add(self, node):
        # how to add node to end of doubly linked list
        # 1 -> 2 -> 3 -> 4 -> tail
        temp = self.tail.prev
        temp.next = node
        node.prev = temp

        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        # we just take the node prev and set it to the node's next
        # and vice versa
        temp1 = node.prev
        temp2 = node.next

        temp1.next = temp2
        temp2.prev = temp1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)