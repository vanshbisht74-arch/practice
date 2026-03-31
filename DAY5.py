# #Doubly linked list 
# #creting a node in doublby linked list
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.prev=None
#         self.next=None

# class doublylinkedlist:
#     def __init__(self):
#         self.head=None
    
#     def insert_at_head(self,val):
#         new_node=node(val)
#         if self.head is None:
#             self.head=new_node
#         else:
#             new_node.next=self.head
#             self.head.prev=new_node
#             self.head=new_node

# #insert at end 
# def insert_end(self,val):
#     new_node=node(val)
#     if self.head is None:
#         self.head=new_node

#     else:
#         temp=self.head
#         while temp is not None:
#             temp=temp.next
#         temp.next=new_node
#         new_node.prev=temp
#stack impletation of queue
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=None
#push at the head
    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def pop(self):
        if self.head is None:
            print("STACK UNDERFLOW")
        
        poped=self.head.data
        self.head=self.head.next
        return poped 
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="=>")
            temp=temp.next
        print("None")


