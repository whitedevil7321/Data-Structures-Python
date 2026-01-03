class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node



    def insert_at_end(self, data):
        if self.head is None:
            print("The list is empty, inserting at the beginning.")   
            self.insert_at_beginning(data)

        else:
            itr=self.head
            while itr.next:
                itr=itr.next

            itr.next=Node(data,None)


    def print_list(self):
        if self.head is None:
            print("The List Is Empty")
            return
        
        itr=self.head

        liststr=''
        while itr:
            liststr+=str(itr.data)+' --> '
            itr=itr.next

        print(liststr+'None')




    def insert_inbetween(self,data,position):
        if position==0:
            self.insert_at_beginning(data)
            return
        itr=self.head
        count=0
        while itr:
            if count==position-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            else:
                itr=itr.next
                count+=1


    def delete_from_end(self):
        if self.head is None:
            print("The list is empty, nothing to delete.")
            return

        if self.head.next is None:
            self.head=None
            return

        itr=self.head
        while itr.next.next:
            itr=itr.next

        itr.next=None


if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_at_end(5)
    ll.insert_at_end(10)
    ll.insert_at_beginning(2)
    ll.insert_at_end(15)
    ll.insert_inbetween(7,2)
    ll.delete_from_end()
    ll.print_list()            




