class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        
    def length(self) -> int:
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.length():
            return -1
        else:
            count=0
            itr=self.head
            while itr: 
                if count == index:
                    return itr.val
                itr=itr.next
                count+=1
            
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is None:
            self.head = Node(val)
        else:
            node=Node(val,self.head)
            self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            self.addAtHead(val)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length():
            return
        elif index == 0:
            self.addAtHead(val)
            return
        else:
            count=0
            itr=self.head
            while itr: 
                if count == index-1:
                    itr.next=Node(val,itr.next)
                    break
                itr=itr.next
                count+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.length() or index < 0:
            return -1
        count=0
        itr=self.head
        prev=self.head
        while itr:
            if count == index:
                prev.next=itr.next
                break
            elif count == index:
                self.head=self.head.next
                break
            prev=itr
            itr=itr.next
            count+=1
    
    def print(self) -> str:
        itr=self.head
        st=''
        while itr:
            st+=str(itr.val)+'-->'
            itr=itr.next
        print(st)
            


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
#obj.addAtHead(3)
obj.print()
obj.addAtTail(3)
#obj.addAtTail(8)
obj.print()
obj.addAtIndex(1,2)
#obj.addAtIndex(3,5)
obj.print()
print(obj.get(1))
obj.deleteAtIndex(0)
obj.print()
print(obj.get(0))

