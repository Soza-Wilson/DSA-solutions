class BinarySearchTreeNode:
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
                self.left = BinarySearchTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            
            else:
                self.right = BinarySearchTreeNode(data)
        



    def in_order_tranvesal(self):
        output  = []
       

        if self.left:
            output += self.left.in_order_tranvesal()

        output.append(self.data)

        if self.right:
            output += self.right.in_order_tranvesal()

        return output
    

    def get_min(self):
        if self.left == None:
            return self.data
        else:
            return self.left.get_min()
        
    def get_max(self):
        if self.right == None:
            return self.data
        else:
            return self.right.get_max()

    
    
    def delete_by_min(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_by_min(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_by_min(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.get_min()
            self.data = min_val
            self.right = self.right.delete_by_min(min_val)

        return self
    

    def delete_by_max(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_by_max(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete_by_max(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            max_val = self.left.get_max()
            self.data = max_val
            self.left = self.left.delete_by_max(max_val)
                

        return self

       


def build_tree(data):
    tree = BinarySearchTreeNode(data[0])
    for i in range(len(data)):
        tree.add_child(data[i])
        
     
    return tree
    




if __name__ == "__main__":
    data = [15,12,7,14,27,20,23,88]
    tree = build_tree(data)

    print("in order tranvesal" , tree.in_order_tranvesal())
    print("min", tree.get_min())
    print("max", tree.get_max())
    delete_value =12
    tree.delete_by_max(delete_value)
    print("Deleted ",delete_value, tree.in_order_tranvesal())
    print([12,32,12] + [12,32,11])