class binarytree:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def addchild(self, data):

        if data < self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left = binarytree(data)
        elif data > self.data:
            if self.right:
                self.right.addchild(data)
            else:
                self.right = binarytree(data)
        else:
            return

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

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

    def calculatesum(self):
        value = self.inorder()
        return sum(value)


def buildtree(elements):
    print("Building tree with elements", elements)
    root = binarytree(elements[0])

    for i in range(1, len(elements)):
        root.addchild(elements[i])

    return root


if __name__ == "__main__":
    numbers = [5, 6, 6, 9, 7, 3]
    number_tree = buildtree(numbers)
    print("Inorder traversal is ", number_tree.inorder())
    print("Preorder traversal is ", number_tree.preorder())
    print("Postorder traversal is ", number_tree.postorder())
    print("Maximum no is ", number_tree.find_max())
    print("Minimum no is ", number_tree.find_min())
    print("Total sum is ", number_tree.calculatesum())
