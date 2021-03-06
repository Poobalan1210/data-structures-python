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


def buildtree(elements):
    print("Printing trees with elements", elements)
    root = binarytree(elements[0])

    for _ in range(1, len(elements)):
        root.addchild(elements[_])

    return root


if __name__ == "__main__":
    names = ['poobalan', 'sai', 'kishore', 'sugash']
    name_tree = buildtree(names)
    print(name_tree.search('poobalan'))
    print(name_tree.inorder())

    numbers = [5, 3, 4, 9, 8, 3]
    number_tree = buildtree((numbers))
    print(number_tree.preorder())
    print(number_tree.search(10))
