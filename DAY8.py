#IMPLETATION OF STACK USING LINKED LIST

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None   # head = top of stack

    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack Underflow")
            return None
        removed = self.head
        self.head = self.head.next
        return removed.val
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.val

    def is_empty(self):
        return self.head is None