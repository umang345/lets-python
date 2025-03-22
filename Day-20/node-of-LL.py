#  Create a Node of LL

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None 

def print_LL(head):
    while(head!=None):
        print(head.data)
        head = head.next

    return

first = Node(1)
second = Node(2)
third = Node(3)

print(id(first), id(second), id(third))

first.next = second
second.next = third

print(first.next)

head = first 