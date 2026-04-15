user_input = input("Enter a mathematical expression: ")
new = []

# Check for alphabetic characters
for value in user_input:
    if value.isalpha():
        print("An expression is not valid.")
        break
    else:
        new.append(value)

result = 0
j = len(new)

# Convert characters to integers where applicable
for i in range(len(new)):
    if new[i].isdigit():
        new[i] = int(new[i])

# Function to perform basic arithmetic operations
def perform_operation(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

# Evaluate the expression
while j > 0:
    for i in range(len(new)):
        if new[i] in {'*', '/', '+', '-'}:
            result = perform_operation(new[i], new[i - 1], new[i + 1])
            new[i - 1:i + 2] = [result]  # Replace the operator and its operands with the result
            j -= 2
            break
    else:
        break  # Break the while loop if no operations are performed

print("Processed expression result:", new[0])
