class TreeNode:

    # creating a tree node

    def __init__(self,data):
        self.data = data 
        self.children = []
        self.parent = None

    #  creating tree children 
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    # first we are printing tree data 
    # if the node is not  a leaf node we are iteratin through the children and calling the print_tree functio for each child

    def print_tree(self):
        space = ' ' * self.get_level() *3
        prefix = space + '|--' if self.parent else ""
        print (prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


    
def build_tree():
    root = TreeNode("Electronics")
   

    # creating braches and their children
    # laptop
    laptop = TreeNode('laptop')
    root.add_child(laptop)
    laptop.add_child(TreeNode('lenovo'))
    laptop.add_child(TreeNode('accer'))
    laptop.add_child(TreeNode('HP'))


    # cellphone

    cellphone = TreeNode('cellphone')
    root.add_child(cellphone)
    cellphone.add_child(TreeNode('Mi'))
    cellphone.add_child(TreeNode('sumsung'))
    cellphone.add_child(TreeNode('honna'))


    # Tv
    tv = TreeNode('tv')
    root.add_child(tv)
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('sumsang'))
    tv.add_child(TreeNode('sony'))





    


    
    return root

if __name__ =='__main__':
    root = build_tree()
    root.print_tree()
    pass