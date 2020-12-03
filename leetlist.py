class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class doublylist:
    def __init__(self):
        self.head=None

    def insertatbeginning(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            self.head = Node(data, next=self.head)

    def length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insertatend(self, data):
        if self.head is None:
            self.insertatbeginning(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, prev=itr)

    def print(self):
        itr = self.head
        istr = ''
        while itr:
            istr += str(itr.data) + '-->'
            itr = itr.next
        print(istr)

    def insertval(self,datalist):
        for i in datalist:
            l.insertatend(i)
        return

    def swapval(self):
        n=self.length()
        it=''
        it+=str(self.head.data)+'-->'
        itr1=self.head.next
        itr2=self.head.next
        while itr2.next:
            itr2=itr2.next
        d=l.length()-1
        c=1
        while c <= d:
            if c%2 != 0:
                it += str(itr2.data) + '-->'
                itr2 = itr2.prev
            else:
                it += str(itr1.data) + '-->'
                itr1 = itr1.next
            c+=1
        print(it)

    def swapval2(self):
        if not self.head:
            return
        itr1=self.head.next
        itr2=self.head.next
        while itr2.next:
            itr2=itr2.next
        c=1
        n=l.length()//2
        while c < n:
            if itr1 is not None and itr2 is None:
                temp=itr2.prev
                itr2.prev=itr1.prev
                itr2.next=itr1.next
                itr1.prev=temp
                itr1.next=None
            else:
                temp=itr2.next
                itr2.next=itr1.next
                itr1.next=temp
                temp=itr2.prev
                itr2.prev=itr1.prev
                itr1.prev=temp
            c+=1
            itr1=itr1.next
            itr2=itr2.prev






l=doublylist()
l.insertval([1,2,3,4,5,6,7,8,9])
l.print()
l.swapval2()
l.print()
