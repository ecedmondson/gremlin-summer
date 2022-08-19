class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head):
        self.head = Node(head)
        self.last = self.head
        self.first = self.head

    def insert(self, val):
        new = Node(val)
        self.last.next = new
        new.prev = self.last
        self.last = new

    def delete(self, val):
        """deletes first occurence of val"""
        ptr = self.head
        assert ptr, f"Empty linked list!"
        while ptr.val != val:
            ptr = ptr.next
            if ptr == self.last:
                raise Exception(f"{val} not in linked list!")
        next = ptr.next
        prev = ptr.prev
        prev.next = next
        next.prev = prev
        if ptr == self.head:
            self.head = next

    def print(self):
        """prints as list"""
        actual_list = []
        ptr = self.head
        while ptr is not None:
            actual_list.append(ptr.val)
            ptr = ptr.next
        print(actual_list)

