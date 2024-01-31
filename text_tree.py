class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinarySearchTree(data)


    def in_order_travesal(self):
        if self.data is None:
            print('Tree is empty')
            return
        output = []
        if self.left:
            output += self.left.in_order_travesal()
        
        output.append(self.data)

        if self.right:
            output += self.right.in_order_travesal()
        
        return output
    
    def pre_order_tranvesal(self):

        if self.data is None:
            print('Tree is empty')
            return
        output = []
        output.append(self.data)
        if self.left:
            output += self.left.in_order_travesal()
        if self.right:
            output += self.right.in_order_travesal()
        
        return output

    def post_order_tranvesal(self):

        if self.data is None:
            print('Tree is empty')
            return
        output = []
       

        if self.left:
            output += self.left.in_order_travesal()
        if self.right:
            output += self.right.in_order_travesal()

        output.append(self.data)
        
        return output
    
    def get_min(self):
        if self.left is None:
            return self.data
        else: 
            return self.left.get_min()
        

    def get_max(self):
        if self.right is None:
            return self.data
        else:
            self.right.get_max()

    def delete_by_max(self,val):
        
       
        
        # first we have to traverse through the tree 

        if val < self.data:
            if self.left:
                self.left = self.left.delete_by_max(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete_by_max(val)
        # if both left and right are empty that means our value is not found in the tree, we return None 
        else:
            if self.left and self.right is None:
                return None
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # getting the max value from left side of the val node 
            max_val = self.left.get_max()
            # setting the val of the current node to the value of the max_val
            self.data = max_val
            # removing the duplicate 
            self.left = self.left.delete_by_max(max_val)
        
        return self



    def delete_by_min(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_by_min(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete_by_min(val)

        else:
            if self.left and self.right is None:
                return None 
            if self.left is None:
                return self.right
            
            elif self.right is None:
                return self.left
            
            min_val = self.right.get_min()
            self.data = min_val
            self.right = self.right.delete_by_min(val)
        return self
            
def buildTree(data):
    binaryTree = BinarySearchTree(data[0])
    for i in range(len(data)):
        binaryTree.add_child(data[i])
    return binaryTree


if __name__ == '__main__':
    data = [15,12,7,9,1,2,4,10]
    tree = buildTree(data)
    print(tree.in_order_travesal())
    tree.delete_by_min(7)
    print(tree.in_order_travesal())
    print(tree.get_max())
    

    
