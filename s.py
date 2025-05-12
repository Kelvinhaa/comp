#COMP10001 TESTING & STUDY
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self) -> None:
        self.head = Node()
    def __contains__(self, data):

        cur = self.head
        while cur.next != None:
            if cur.data == data:
                return True
            cur = cur.next
        return False
    def length(self):
        pass
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

ll = Linkedlist()
ll.append(10)
ll.append(5)
ll.append(18)
ll.prepend(100)
print(ll)