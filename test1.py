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

    def print(self):
        if self.head is None:
            print("empty list")
        itr=self.head
        istr=""
        while itr.next:
            istr += str(itr.data)+"-->"
            itr = itr.next
        istr += str(itr.data)
        print(istr)




if __name__ =="__main__":
    l=Linkedlist()
    l.insertatbeginning(5)
    l.insertatbeginning(5)
    l.print()
