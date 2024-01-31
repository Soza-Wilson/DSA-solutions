class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None


    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level


    def print_tree(self,level):
        space = ' '* self.get_level() * 3
        prifix = space+'|--' if self.parent else ''
        if self.get_level() <= level:
            print(prifix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_tree():
    root = TreeNode('Grobal')

    #  data for Malawi branch and all its leafs 
    malawi = TreeNode('Malawi')
    root.add_child(malawi)
    central = TreeNode('central')
    northen = TreeNode('northen')
    central.add_child(TreeNode('lilongwe'))
    northen.add_child(TreeNode('lunphi'))
    malawi.add_child(central)
    malawi.add_child(northen)
  


    #  data for USA branch and all its leafs

    usa = TreeNode('USA')
    root.add_child(usa)
    new_jersey = TreeNode('New Jersey')
    california = TreeNode('California')
    usa.add_child(new_jersey)
    usa.add_child(california)
    new_jersey.add_child(TreeNode('Princeton'))
    new_jersey.add_child(TreeNode('Trenton'))
    california.add_child(TreeNode('San Francisco'))
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('palo Alto'))


    return root

if __name__ == '__main__':
    root = build_tree()
    root .print_tree(1)
    root .print_tree(2)
    root .print_tree(3)
    
    
