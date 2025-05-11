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



class Queue:
    def __init__(self):
        self.front = None  # First to come out
        self.rear = None   # Last to go in
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None  # or raise an error
        removed = self.front
        self.front = self.front.next
        if self.front is None:  # If the queue is now empty
            self.rear = None
        self.size -= 1
        return removed.value

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

    def __len__(self):
        return self.size

    def __repr__(self):
        values = []
        current = self.front
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)

# Example usage
if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q)             # 10 -> 20 -> 30
    print(q.dequeue())   # 10
    print(q.peek())      # 20
    print(len(q))        # 2
