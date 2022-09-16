class Node(object): 
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev_node = prev_node

class LinkedList(object):
    def __init__(self, values=[]):
        self.head = None
        for value in values:
            self.insert(value)
    
    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev_node = current
            return new_node
    
    def delete(self, value):
        if not self.head:
            return "Value not in list bc list is empty"

        current = self.head
        while current.next:
            if current.value == value:
                if current.prev_node is None:
                    self.head = current.next
                    return current
                current.prev.next = current.next
                return current
            current = current.next
        return "Value not in list"
    

def sum_two_lists(first, second):
    def convert_to_num(list_head):
        current = list_head
        num = []
        while current:
            num.insert(0, str(current.value))
            current = current.next
        return num
        
    num1 = int("".join(convert_to_num(first.head)))
    num2 = int("".join(convert_to_num(second.head)))
    summed = str(num1 + num2)[::-1]
    
    answer = LinkedList(values=summed)
    return answer.head

def is_palindrome(linked_list):
    if not linked_list.head:
        return "Nothing to see here"
    
    fwd_pointer = linked_list.head
    backward_pointer = linked_list.head
    list_length = 0
    while backward_pointer.next:
        backward_pointer = backward_pointer.next
        list_length += 1
    
    for _ in range(list_length // 2):
        if fwd_pointer.value != backward_pointer.value:
            return "not a palindrome"
        fwd_pointer = fwd_pointer.next
        backward_pointer = backward_pointer.prev_node
    
    return "Palindrome!"

def intersecting_node(ll1, ll2):
    """What I came up with first- so slow it wouldn't run on Leetcode agasint large lists"""
    current_ll1_node = ll1.head
    while current_ll1_node:
        current_ll2_node = ll2.head
        while current_ll2_node:
            if current_ll1_node == current_ll2_node:
                return current_ll1_node
            current_ll2_node = current_ll2_node
        current_ll1_node = current_ll1_node
    return None

def intersecting_node_optimized_per_book(ll1, ll2):
    """
    Method recommended by the book
    Run through each linked list to get the lengths and the tails
    Compare the tails. If they are different (by ref, not by val) return immediately
    Set two pointers to the start of each linked list
    On the longer linked list, advance fwd to make them both the same length
    Traverse on each linked list until the pointers are the same
    """
    length_a = 0
    length_b = 0
    last_a = ll1.head
    last_b = ll2.head
    # Get length of each list, and make sure last node is the same.
    # If not, we don't have any intersection
    while last_a.next:
        last_a = last_a.next
        length_a += 1
    while last_b.next:
        last_b = last_b.next
        length_b += 1
    if last_a != last_b:
        return None
    
    # Now, find point of convergence
    current_a = ll1.head
    current_b = ll2.head
    if length_a > length_b:
        diff = length_a - length_b
        while diff:
            current_a = current_a.next
            diff -= 1
    elif length_b > length_a:
        diff = length_b - length_a
        while diff:
            current_b = current_b.next
            diff -= 1
    while current_a != current_b:
        current_a = current_a.next
        current_b = current_b.next
    
    return current_a

def intersecting_nodes_cache(ll1, ll2):
    """Based off another person's solution on Leetcode- still slow though!"""
    visited = set()
    current_a = ll1.head
    while current_a:
        visited.add(current_a)
        current_a = current_a.next
    
    current_b = ll2.head
    while current_b:
        if current_b in visited:
            return current_b
        current_b = current_b.next
    return None

def is_list_circular(llist):
    """This is what I came up with, based on my attempts at the previous problem"""
    visited = set()
    current = llist.head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

def is_list_circular_fast_runner_slow_runner(llist):
    """This is based on what the book says, w/ the fast and slow pointer"""
    slow_pointer = llist.head
    fast_pointer = llist.head
    while fast_pointer and fast_pointer.next:
        slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True
    return False
