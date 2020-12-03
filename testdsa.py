class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def insertatbeginnig(self,data):
        node=Node(data,self.head)
        self.head=node
        return

    def insertatend(self,data):
        if self.head is None:
            node=Node(data)
            self.head=node
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            node=Node(data)
            itr.next=node
        return

    def length(self):
        itr=self.head
        count=0
        while itr:
            count += 1
            itr=itr.next
        return count

    def remove(self,index):
        if index < 0 or index > l.length():
            raise Exception("Invalid list")
        count = 0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count +=1

    def removeval(self,data):
        if self.head is None:
            print("list is empty")
        itr1=self.head
        itr2=self.head
        if itr1.data == data:
            self.head=itr1.next
            return
        while itr1.next:
            itr1=itr1.next
            if data == itr1.data:
                itr2.next=itr1.next
                break
            itr2=itr2.next


    def insertat(self,index,data):
        if index < 0 and index > self.length():
            raise Exception("Invalid list")
        itr=self.head
        if index == 0:
            self.insertatbeginnig(data)
            return
        else:
            count = 0
            while itr:
                if count == index-1:
                    itr.next=Node(data,itr.next)
                    break
                itr=itr.next
                count += 1

    def insertval(self,datalist):
        for i in datalist:
            l.insertatend(i)
        return

    def insertafter(self,prevdata,insdata):
        if self.head is None:
            l.insertatbeginnig(insdata)
        itr1=self.head
        while itr1:
            if itr1.data == prevdata:
                itr1.next=Node(insdata,itr1.next)
                break
            itr1=itr1.next

    def print(self):
        if self.head is None:
            print("list empty")
        isrt=""
        itr=self.head
        while itr:
            if itr.next is not None:
                isrt += str(itr.data) +"-->"
                itr=itr.next
            else:
                isrt +=str(itr.data)
                break
        print(isrt)
        return


if __name__ == "__main__":
    l=Linkedlist()
    l.insertatbeginnig(1)
    l.print()
    l.insertatbeginnig(5)
    l.print()
    l.insertatbeginnig(10)
    l.print()
    l.insertatend(100)
    l.print()
    l.insertat(0,50)
    l.print()
    print(l.length())
    l.remove(2)
    l.print()
    print(l.length())
    l.removeval(50)
    l.print()
    l.removeval(100)
    l.print()
    l.insertval([7,8,9,10])
    l.print()
    l.insertafter(1,6)
    l.print()
    l.insertafter(10,0)
    l.print()
