# Function to define precedence of operators
def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0


# Function to convert infix to postfix
def infix_to_postfix(expression):

    stack = []      # Stack for operators
    postfix = ""    # Final result string

    for char in expression:

        # If operand → add directly to postfix
        if char.isalnum():
            postfix = postfix + char

        # If opening bracket → push to stack
        elif char == "(":
            stack.append(char)

        # If closing bracket → pop until '('
        elif char == ")":
            while stack and stack[-1] != "(":
                postfix = postfix + stack.pop()
            stack.pop()   # Remove '('

        # If operator
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix = postfix + stack.pop()
            stack.append(char)

    # Pop remaining operators
    while stack:
        postfix = postfix + stack.pop()

    return postfix


# ------------------------------
# Calling the function
# ------------------------------

expr = input("Enter infix expression: ")
expr = expr.replace(" ", "")   # Remove spaces

result = infix_to_postfix(expr)

print("Postfix Expression:", result)