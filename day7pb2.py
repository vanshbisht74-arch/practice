class StackAdt:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) == 0:
            print("Stack Underflow!")
            
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            print("Stack Underflow!")
            
        else:
            return self.items[-1]

    def isempty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Displayed Items", self.items)


s = StackAdt()
s.push(5)
s.push(6)
s.push(7)
s.pop()
print(s.size())


def balancecheck(expression):
    stack = StackAdt()

    for char in expression:
        if char in "([{":
            stack.push(char)

        elif char in ")]}":
            if stack.isempty():
                print("INVALID INPUT")
                

            top = stack.pop()

            if (top == "(" and char != ")") or \
               (top == "{" and char != "}") or \
               (top == "[" and char != "]"):
                print("INVALID INPUT")
                

    if stack.isempty():
        print("BALANCED")
    else:
        print("INVALID INPUT")

