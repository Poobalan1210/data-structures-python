class binarytree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def addchild(self, data):
        if self.data == data:
            return
        elif self.data > data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left = binarytree(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right = binarytree(data)

    def search(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def inorder(self):
        output = []
        if self.left:
            output += self.left.inorder()
        output.append(self.data)
        if self.right:
            output += self.right.inorder()
        return output

    def preorder(self):
        output = []
        output.append(self.data)
        if self.left:
            output += self.left.preorder()
        if self.right:
            output += self.right.preorder()

        return output

    def postorder(self):
        output = []
        if self.left:
            output += self.left.postorder()
        if self.right:
            output += self.right.postorder()
        output.append(self.data)

        return output


if __name__ == "__main__":
    obj = binarytree(6)
    obj.addchild(5)
    obj.addchild(10)
    obj.addchild(2)
    print(obj.search(10))
    print(obj.inorder())
    print(obj.preorder())
    print(obj.preorder())
