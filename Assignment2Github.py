class Node:
    def __init(self,data):
        self.data = data;
        self.next = None;
        self.prev = None;

class DoublyList:
    
    def _init_(self):
        self.head = None

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enque(self,data):
        if(self.head == None):
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node.prev = cur
            new_node.next = None
            
    def deque(self, data):
        pass

    def display(self):
        if self.size == 0:
            print("No element")
            return
        first = self.head
        print(first.element)
        first = first.next
        while first:
            print(first.element)
            first = first.next
            
dlist = DoublyList()
dlist.enque(1)
dlist.enque(2)
dlist.enque(3)
dlist.enque(4)

dlist.print_list()
