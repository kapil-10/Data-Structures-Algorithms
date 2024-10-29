class binarysearchtree:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self. right = None

    def add_child(self,data):
        # check for dublicates
        if data == self.data:
            return
        
        # add child to left subtree
        if data < self.data:

            # check if left subtree has any nodes
            if self.left:
                self.left.add_child(data)
            
            else:
                self.left = binarysearchtree(data)
        
        # add child to left subtree
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binarysearchtree(data)

    def inordertraversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.inordertraversal()
        # visit center node
        elements.append(self.data)
        #visit right tree
        if self.right:
            elements += self.right.inordertraversal()
        return elements
    
    def preordertraversal(self):
        elements = []
        # visit center node
        elements.append(self.data)
        #visit left tree
        if self.left:
            elements += self.left.preordertraversal()
        if self.right:
            elements += self.right.preordertraversal()
        return elements
    
    def postordertraversal(self):
        elements = []
        #visit left 
        if self.left:
            elements += self.left.postordertraversal()
        # visit right tree
        if self.right:
            elements += self.right.postordertraversal()
        # visit center
        elements.append(self.data)
        return elements 
    
    def search(self,key):
        if key == self.data:
            return True
        if key < self.data: # key might be in left sub tree
            if self.left:
                return self.left.search(key)
            else:
                return False
        if key > self.data: # key might be in right sub tree
            if self.right:
                return self.right.search(key)
            else:
                return False
            
    def findmin(self):
        if self.left is None:
            return self.data
        else:
            if self.left:
                return self.left.findmin()
    
    def findmax(self):
        if self.right is None:
            return self.data
        else:
            if self.right:
                return self.right.findmax()
            
    def delete(self,val):
        if val < self.data:
            # check for left subtree
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        
        else:
            # case 1  a node with no left and right childs
            if self.left is None and self.right is None:
                return None 
            # case when we have no left child
            if self.left is None:
                return self.right
            # case when we have right child
            if self.right is None:
                return self.left
            
            min_val = self.right.findmin()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def calculatesum(self):
        total = 0
        for value in self.inordertraversal():
            total += value
        return total
    
    def height(self):
        leftheight = self.left.height() if self.left else 0
        rightheight = self.right.height() if self.right else 0
        return 1 + max(leftheight,rightheight)

        
def buildtree(elements):
    root = binarysearchtree(elements[0])
    for value in range(1,len(elements)):
        root.add_child(elements[value])
    return root


if __name__ == '__main__':
    numbers = [15,12,27,7,14,20,88,23]
    numbers_tree = buildtree(numbers)
    print('In_order_traversal',numbers_tree.inordertraversal())

    print('Pre_order_traversal',numbers_tree.preordertraversal())

    print('Post_order_traversal',numbers_tree.postordertraversal())

    print('Lets search for value 88 :',numbers_tree.search(12))

    print('The min value in tree is :',numbers_tree.findmin())

    print('The max value in tree is :',numbers_tree.findmax())

    print('The total sum is :',numbers_tree.calculatesum())

    print('The height is :',numbers_tree.height())

    print('Before deletion',numbers_tree.inordertraversal())

    numbers_tree.delete(88)

    print('After deletion',numbers_tree.inordertraversal())



