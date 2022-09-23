class MyStack:
    def __init__(self):
        self.stack = []
    
    def push(self, val: int):
        self.stack.append(val)
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    
    def pop(self):
        if not self.is_empty():
            val = self.stack[-1]
            self.stack = self.stack[:-1]
            return val
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0


class MyQueue:

    def __init__(self):
        self.first_stack = MyStack()
        self.second_stack = MyStack()

    def _shift_stacks(self):
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop())
    
    def push(self, x: int) -> None:
        self.first_stack.push(x)

    def pop(self) -> int:
        self._shift_stacks()
        if not self.empty():
            return self.second_stack.pop()

    def peek(self) -> int:
        self._shift_stacks()
        if not self.empty():
            return self.second_stack.peek()

    def empty(self) -> bool:
        return self.first_stack.is_empty() and self.second_stack.is_empty()
        
