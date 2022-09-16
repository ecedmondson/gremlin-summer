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

    def insert_and_retrieve(self, val):
        self.insert(val)
        return self.last

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

        
        
        
    
    
# Round 2 starts here

def remove_dups(linked_list):
    head = linked_list.head
    already = {}
    while head != None:
        if head.val not in already:
            already[head.val] = True
        else:
            prev = head.prev
            nxt = head.next
            prev.next = nxt
            nxt.prev = prev
        head = head.next 

def kth_to_last(ll, k):
    # what to do if k > len(ll)? 
    # like what to return? None, reverse indexing? idk
    # don't handle it right now
    base = ll.head
    ind = 0
    while base:
        if ind == k:
            ll.head = base
            base.prev = None
            return ll
        ind += 1
        base = base.next

print("ktl")
ktl = DLL(1)
for x in range(2, 10):
    ktl.insert(x)

ktl.print()
kth_to_last(ktl, 5)
ktl.print()

   
print("delete middle node")
print("this one says to use singly linked list. my implementation is DLL, so i'm just not going to call prev")
def delt_mid(middle_node):
    cur = middle_node
    nxt = middle_node.next
    while nxt:
        cur.val = nxt.val
        cur = nxt
        nxt = nxt.next

dm = DLL(1)
for x in range(2, 7):
    dm.insert(x)
mid = dm.insert_and_retrieve(8)
for x in range(9, 15):
    dm.insert(x)

dm.print()
delt_mid(mid)
dm.print()

print("i seem to delete two nodes here. not sure how to get around that without access to prev")

print("partitioning, i guess")
 
