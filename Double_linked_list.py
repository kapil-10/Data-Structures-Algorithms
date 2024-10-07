class Node:
    def __init__ (self,data,prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next

class double_linked_list():
    def __init__ (self):
        self.head = None
    
    def get_length(self):
        if self.head is None:
            return 0
        else:
            count = 0
            itr = self.head 
            while itr:
                count += 1
                itr = itr.next 
        return count
    
    def insert_at_front(self,data):
        if self.head is None:
            node = Node(data,None,self.head)
            self.head = node
        else:
            new_node = Node(data,None,self.head)
            self.head.prev = new_node
            self.head = new_node

    def insert_at_rear(self,data):
        if self.head is None:
            self.insert_at_front(data)
        else:
            itr = self.head
            while itr.next: # move till the last node
                itr = itr.next # last node next which is null 
            node = Node(data,itr,None)
            itr.next = node
            
    def insert_at(self,data,index):
        if index < 0 or index > self.get_length():
            print ('Invalid index length')
            return
        if index == 0:
            self.insert_at_front(data)
            return
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index -1:
                     node = Node(data,itr,itr.next)
                     node.next = itr.next
                     itr.next = node
                     break
                itr = itr.next
                count += 1

    def insert_array_values (self,array_input):
        for input in array_input:
            if self.head is None:
                self.insert_at_front(input)
            else:
                self.insert_at_rear(input)

    def remove_at_index (self,index):
        if index < 0 or index > self.get_length():
            raise Exception ('Invalid index')
        if index == 0:
            self.head = self.head.next
        itr = self.head 
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                    break
            itr = itr.next
            count += 1

    def print_forward(self):
        if self.head is None:
            print('Double_linked_list is empty')
            return []
        itr = self.head
        container =[]
        while itr:
            container.append(itr.data)
            itr = itr.next
        return container
    
    def print_backwords(self):
        if self.head is None:
            print('Double_linked_list is empty')
            return []
        itr = self.head
        container = []
        while itr.next:
            itr = itr.next
        
        while itr:
            container.append(itr.data)
            itr = itr.prev
        return container
        

if __name__ == '__main__':

    dll = double_linked_list()
    dll.get_length()
    dll.insert_at_front(1)
    dll.insert_at_rear(2)
    numbers = [3,5,6,7,8,9,10]
    dll.insert_array_values(numbers)
    dll.insert_at(4,5)
    dll.remove_at_index(6)
    print('Forward Traversal ',dll.print_forward())
    print('Backword Traversal ',dll.print_backwords())