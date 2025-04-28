#COMP10001 TESTING & STUDY
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self) -> None:
        self.head = Node()
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def insert(self, data, index):
        pass
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
