class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head): # Function to reverse a linked list
    prev = None # Initialize previous node to None
    current = head # Start with the head of the list
    while current is not None: # Traverse the list until the end
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev to the current node
        current = next_node       # Move to the next node
    return prev  # At the end, prev will be the new head of the reversed list
# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> None
head = listNode(1)
head.next = listNode(2)
head.next.next = listNode(3)
# Reversing the linked list
reversed_head = reverse_linked_list(head)
# Printing the reversed linked list: 3 -> 2 -> 1 -> None
current = reversed_head
while current is not None:
    print(current.value)  # Output the value of the current node
    current = current.next  # Move to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def delete_at_head(self):
        if self.head is None:
            raise IndexError('List is empty')
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    def delete_at_tail(self):
        if self.head is None:
            raise IndexError('List is empty')
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        current = self.head
        while current.next.next is not None:
            current = current.next
        data = current.next.data
        current.next = None
        self.size -= 1
        return data