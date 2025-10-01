class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.extend(item)
        return len(self.stack)

    def pop(self):
        if self.stack == []:
            return "Stack is empty!"
        else:
            remove = self.stack.pop()
            return remove

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True

    def size(self):
        return len(self.stack)


s = stack()
print("Size after push:", s.push([1, 2, 3, 4, 5]))
print("Top element:", s.peek())

print("pop:", s.pop())
print("pop:", s.pop())
print("pop:", s.pop())
print("pop:", s.pop())
print("pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())