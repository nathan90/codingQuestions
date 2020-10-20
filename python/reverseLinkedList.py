# Program to reverse linked list
# Node class
class Node:
    def __init__(self, data):
        self.data = data,
        self.next = None

class LinkedList:
    # initialize head
    def __init__(self):
        self.head = None

    # function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    # function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("given linked list")
llist.printList()
llist.reverse()
print('reversed linked list')
llist.printList()