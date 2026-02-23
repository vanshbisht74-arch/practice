# Node class
class Node:
    def __init__(self, data):
        self.data = data      # value
        self.next = None      # pointer to next node


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # -----------------------------
    # Traverse / Display list
    # -----------------------------
    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

    # -----------------------------
    # Insert at beginning  O(1)
    # -----------------------------
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # -----------------------------
    # Insert at end  O(n)
    # -----------------------------
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    # -----------------------------
    # Insert at position (0-based index)  O(n)
    # -----------------------------
    def insert_position(self, data, pos):
        new_node = Node(data)

        if pos == 0:
            self.insert_beginning(data)
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    # -----------------------------
    # Delete from beginning  O(1)
    # -----------------------------
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # -----------------------------
    # Delete from end  O(n)
    # -----------------------------
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        
        temp.next = None

    # -----------------------------
    # Delete at position  O(n)
    # -----------------------------
    def delete_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos == 0:
            self.delete_beginning()
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

    # -----------------------------
    # Search element  O(n)
    # -----------------------------
    def search(self, key):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1
        return -1

    # -----------------------------
    # Length of list  O(n)
    # -----------------------------
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count