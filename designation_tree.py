class TreeNode():
    def __init__(self,data):
        self.name = data['name']
        self.designation = data['designation']
        self.children = []
        self.parent = None


    def add_child(self,child):
        child.parent = self
        self.children .append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p= p.parent
        return level
    
    def print_tree(self,type):

        space = ' ' * self.get_level() *3
        prefix = space + '|--' if self.parent else ""
        if type == 'name':
            print(prefix+self.name)
        elif type == 'designation':
            print(prefix+self.designation)
        elif type == 'both':
            print(prefix+self.name,self.designation) 
     
        if self.children:
            for child in self.children:
                child.print_tree(type)

    
def build_tree():
    data = {'name': 'Nilupul', 'designation' : '(CEO)'}
    root = TreeNode(data)



#     creating CTO branch and all its leafs 
    cto = TreeNode({'name' : 'chinmay', 'designation' : '(CTO)' })
    root.add_child(cto)
    infu_H = TreeNode({'name' : 'john', 'designation' : '(Infustructure Head)'}) 
    cto.add_child(infu_H)
    infu_H.add_child(TreeNode({ 'name' : 'Mary', 'designation' : '(Cloud Manager)' }))
    infu_H.add_child(TreeNode({ 'name' : 'andrew', 'designation' : '(App Manager)' }))
    app_Head = TreeNode({'name' : 'aimir', 'designation' : '(Application Head)'})
    cto.add_child(app_Head)

#   Creating 
    hr_head = TreeNode({'name' : 'Gels', 'designation' : '(Hr Head)'})
    root.add_child(hr_head)
    hr_head.add_child(TreeNode({'name' : 'Peter', 'designation' : '(Rectrutment Manager)'}))
    hr_head.add_child(TreeNode({'name' : 'waqas', 'designation' : '(Policy Manager)'}))


    return root


if __name__ == '__main__':
    root = build_tree()
    root.print_tree('name')
    root.print_tree('designation')
    root.print_tree('both')
    
    