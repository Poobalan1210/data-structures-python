
class treenode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def printtree(self, level):
        spaces = ' ' * self.getlevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        if self.getlevel() <= level:
            print(prefix + self.name)
        else:
            pass
        if self.children:
            for child in self.children:
                child.printtree(level)

    def addchild(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = treenode("Global")

    guj = treenode("Gujarat")
    guj.addchild(treenode("Ahmedabad"))
    guj.addchild(treenode("baroda"))

    kar = treenode("Karanataka")
    kar.addchild(treenode("Bangalore"))
    kar.addchild(treenode("Mysore"))

    ind = treenode("India")
    ind.addchild(guj)
    ind.addchild(kar)

    nj = treenode("New Jersey")
    nj.addchild(treenode("Princeton"))
    nj.addchild(treenode("Trenton"))

    cal = treenode("California")
    cal.addchild(treenode("San Francisco"))
    cal.addchild(treenode("Mountain view"))
    cal.addchild(treenode("Palo Alto"))

    usa = treenode("USA")
    usa.addchild(nj)
    usa.addchild(cal)

    root.addchild(ind)
    root.addchild(usa)

    root.printtree(1)


if __name__ == '__main__':
    build_product_tree()
