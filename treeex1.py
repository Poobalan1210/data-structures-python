class treenode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def addchild(self, child):
        child.parent = self
        self.children.append(child)

    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printtree(self, input):
        spaces = " "*self.getlevel()*3
        prefix = spaces+"|__" if self.parent else ""
        if input == "both":
            print(prefix+self.name+' '+'('+self.designation+')')
        elif input == "name":
            print(prefix+self.name)
        else:
            print(prefix+self.designation)
        if self.children:
            for child in self.children:
                child.printtree(input)


def buildtree():
    root = treenode("Nilupul", "CEO")
    vis = treenode("Vishwa", "Infrastructure Head")
    vis.addchild(treenode("Dhaval", "Cloud Manager"))
    vis.addchild(treenode("Abhijit", "App manager"))
    amir = treenode("Aamir", "Application Head")
    chinmay = treenode("Chinmay", "CTO")
    chinmay.addchild(vis)
    chinmay.addchild(amir)
    gels = treenode("Gels", "HR Head")
    gels.addchild(treenode("Peter", "Recruitment Manger"))
    gels.addchild(treenode("Waqas", "Policy Manager"))
    root.addchild(chinmay)
    root.addchild(gels)

    root.printtree("name")  # prints only name hierarchy
    root.printtree("designation")  # prints only designation hierarchy
    root.printtree("both")


if __name__ == '__main__':
    buildtree()
