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

# lazy
DLL = DoublyLinkedList

first_list = DLL(7)
first_list.insert(1)
first_list.insert(6)
first_list.insert(8)

second_list = DLL(5)
second_list.insert(9)
second_list.insert(2)

def sum_lists_reverse(first_list, second_list):
    first = first_list.head
    second = second_list.head
    remainder = None
    use_remainder = False
    new_list = None
    keep_cycle = True
    while keep_cycle:
        sum = getattr(first, "val", 0) + getattr(second, "val", 0)
        if remainder and use_remainder:
            sum = sum + remainder
            use_remainder = False
        if sum > 10:
            sum = sum - 10
            remainder = 1
            use_remainder = True
        if new_list:
            new_list.insert(sum)
        else:
            new_list = DLL(sum)
        first = getattr(first, "next", None)
        second = getattr(second, "next", None)
        if first == None and second == None:
            if use_remainder:
                new_list.insert(remainder)
            new_list.print()
            return

sum_lists_reverse(first_list, second_list)

def get_double_next(node):
    next = node.next
    if next:
        if next.next:
            return 2, next.next
        return 1, next.next
    return 0, None
        
# DLL is doubly linked but make this work for single too       
def is_linked_list_palindrome(linked_list):
    # aha
    # ahha
    # aebea
    # find last
    last = linked_list.head
    while last.next != None:
        last = last.next
    first = linked_list.head
    while last.prev != None:
        if first.val != last.val:
            return False
        last = last.prev
        first = first.next

    return True

palin = DLL("a")
palin.insert("e")
palin.insert("b")
palin.insert("e")
palin.insert("a")

bad = DLL("a")
bad.insert("b")
bad.insert("c")
bad.insert("d")
bad.insert("a")

short = DLL("a")
short.insert("b")
short.insert("a")

even = DLL("a")
even.insert("h")
even.insert("h")
even.insert("a")

print(is_linked_list_palindrome(palin))
print(is_linked_list_palindrome(bad))
print(is_linked_list_palindrome(short))
print(is_linked_list_palindrome(even))

        
        
        
    
    
 
