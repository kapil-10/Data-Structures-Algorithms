class Node:
    def __init__ (self,data,next):
        self.data = data
        self.next = next

class linked_list:
    def _init__ (self):
        self.head = None

    def insert_at_front(self,value):
        node = Node(value,self.head) 
        self.head = node


    def insert_at_end(self,value):
        if self.head is None:
            self.head = Node(value,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(value,None)
    
    def inser_values(self,values_list):
        self.head = None
        for value in values_list:
            self.insert_at_end(value)


    def insert_at_index(self,index,value):
        if index < 0 or index > self.get_length():
            print('Invalid Index')
        if index == 0 :
            self.insert_at_front(value)
            return

        itr = self.head
        count = 0 
        while itr:
            if count == index - 1:
                node = Node(value,itr.next)
                itr.next = node
                break
            count += 1

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        
        return count

        
    
    def print (self):
        if self.head is None:
            print('Linked list is empty')
            return
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data) + ' --> '
                itr = itr.next
            print(llstr)






if __name__ == '__main__':
    ll = linked_list()

    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_front(30)

