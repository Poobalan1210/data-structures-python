class stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def print(self):
        return self.items

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isempty():
            return self.items[-1]

    def isempty(self):
        return self.items == []

    def clearstack(self):
        self.items = []



if __name__ == '__main__':
    s=stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())
    s.pop()
    print(s.print())
    print(s.isempty())
    s.clearstack()
    print(s.isempty())
    print(s.peek())

