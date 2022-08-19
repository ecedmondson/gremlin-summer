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
