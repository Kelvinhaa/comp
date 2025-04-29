#Learning stack and queue here
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
    
    def repr(self):
        items = []
        cur = self.top
        while cur != None:
            items.append(cur.value)
            cur = cur.next
        return items

    def len(self):
        return self.size
        # O(1) - constant time
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        self.size += 1
    
    def pop(self):
        if self.top is None:
            print("stack is empty")
        pop_value = self.top.value
        self.top = self.top.next

        self.size -= 1
        return pop_value
    def peek(self):
        return self.top.value
        
if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(14)
    stack.push(20)
    print(stack.repr())
    print(stack.peek())
    print(stack.pop())
    print(stack.repr())
    print(stack.len())


