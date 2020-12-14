class binarytree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addchild(self, data):

        if data < self.data:
            if self.left:
                return self.left.addchild(data)
            else:
                self.left = binarytree(data)
        elif data > self.data:
            if self.right:
                return self.right.addchild(data)
            else:
                self.right = binarytree(data)
        else:
            return

    def inorder(self):
        output = []
        if self.left:
            output += self.left.inorder()
        output.append(self.data)
        if self.right:
            output += self.right.inorder()
        return output

    def findmax(self):
        if self.right:
            return self.right.findmax()
        return self.data

    def findmin(self):
        if self.left:
            return self.left.findmin()
        return self.data

    def delete(self, value):

        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            maxval = self.left.findmax()
            self.data = maxval
            self.left = self.left.delete(maxval)

        return self


def buildtree(elements):
    root = binarytree(elements[0])

    for i in range(1, len(elements)):
        root.addchild(elements[i])

    return root


if __name__ == "__main__":
    elements = [1, 56, 3, 7, 8, 9, 46]
    result = buildtree(elements)
    print(result.inorder())
    print(result.findmax())
    print(result.findmin())
    result.delete(9)
    print(result.inorder())
