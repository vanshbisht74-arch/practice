#INSERTION SORT IN SINGLY LINKED LIST
class list_node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    
    def getnthNode(self,head,ind):
        temp=head
        for i in range(ind):
            temp=temp.next
        return temp
    
    def getlen(self,head):
        length=0
        temp=head
        while temp is not None:
            temp=temp.next
            length+=1
        return length

    def swapvalues(self,head,j1,j):
        node_j1=self.getnthNode(head,j1)
        node_j=self.getnthNode(head,j)
        node_j1.val=node_j.val
    def assignvalue(self,head,ind,val):
        node=self.getnthNode(head,ind)
        node.val=val
    
    def insertionsort(self,head):
        n=self.getlen(head)
        for i in range(1,n):
            j=i-1
            key=self.getnthNode(head,i).val
            while j>=0 and self.getnthNode(head,j).val>key:
                self.swapvalues(head,j+1,j)        
                j=j-1
            self.assignvalue(head,j+1,key)
        return head