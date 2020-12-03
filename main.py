class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def insertatbeginning(self,data):
        node=Node(data,self.head)
        self.head=node
        return

    def insertatlast(self,data):
        if self.head is None:
            node =Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        return

    def length(self):
        count = 0
        itr=self.head
        while itr:
            count += 1
            itr=itr.next
        return count

    def remove(self,index):
        if index <0 and index > l.length():
            raise Exception("List is empty")

        if index == 0:
            self.head =self.head.next
            return

        count=0
        itr=self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("list is empty")
            return
        itr=self.head
        lstr=""
        while itr:
            lstr+=str(itr.data)+"-->"
            itr=itr.next
        if len(lstr) >0:
            print(lstr)
        else:
            print("empty string")

    def removeval(self,data):
        if self.head is None:
            raise Exception("empty list")
        itr1 = self.head
        itr2 = self.head
        if itr1.data == data:
            self.head=itr1.next
            return
        while itr1:
            itr1=itr1.next
            if itr1.data == data:
                itr2.next = itr1.next
                break
            else:
                itr2=itr2.next


if __name__ == '__main__':
    l=Linkedlist()
    l.insertatbeginning(5)
    l.insertatbeginning(6)
    l.insertatlast(10)
    l.insertatlast(11)
    l.print()
    l.remove(2)
    l.print()
    l.removeval(11)
    l.print()

