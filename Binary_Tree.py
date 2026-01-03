class Binary_tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return    
        
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binary_tree(data)


        else: 
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binary_tree(data)      



    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements.extend(self.left.in_order_traversal())

        elements.extend([self.data])
        if self.right:
            elements.extend(self.right.in_order_traversal())
        return elements        
    


    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements.extend(self.left.pre_order_traversal())

        if self.right:
            elements.extend(self.right.pre_order_traversal())
        return elements
    



    def post_orer_traversal(self):
        elements=[]
        if self.left:
            elements.extend(self.left.post_orer_traversal())

        if self.right:
            elements.extend(self.right.post_orer_traversal())

        elements.extend([self.data])
        return elements        





    def search(self,data):
        if self.data==data:
            return True
        if data<self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
            
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False    





    def find_min(self):
        if self.data is None:
            return None
        if self.left is None:
            return self.data
        return self.left.find_min()
    


    def find_max(self):
        if self.data is None:
            return None
        if self.right is None:
            return self.data
        return self.right.find_max()
    

    def calculate_sum(self):
        elements=self.in_order_traversal()
        return sum(elements)
    


    def Delete(self,data):

        if self.data<data:
            if self.right:
                self.right=self.right.Delete(data)

        elif self.data>data:
            if self.left:
                self.left=self.left.Delete(data)

        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val=self.left.find_max()
            self.data=min_val
            self.left=self.left.Delete(min_val)  

        return self                  
    

if __name__=="__main__":
    numbers=[17,4,1,20,9,23,18,34,18,4,4,4,4,4,4,4,4]
    root=Binary_tree(numbers[0])
    for number in numbers[1:]:
        root.add_child(number)


    print("Root is",numbers[0])
    print("In order traversal gives sorted order")
    print(root.in_order_traversal())    

    print("Pre order traversal gives sorted order")
    print(root.pre_order_traversal())    


    print("Post order traversal gives sorted order")
    print(root.post_orer_traversal())    

    print("Searching for 20:",root.search(20))
    print("Searching for 5:",root.search(5))

    print("Minimum value in the tree is:",root.find_min())
    print("Maximum value in the tree is:",root.find_max())

    print("Sum of all the elements in the tree is:",root.calculate_sum())

    



    print("Tree Before Deletion")
    print(root.in_order_traversal())
    root.Delete(20)
    print("Tree After Deletion of 20")
    print(root.in_order_traversal())