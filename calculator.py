a=float(input("Enter first number"))
b=float(input("Enter a second number"))
print("Enter + for addition")
print("Enter - for addition")
print("Enter *  for multiplication")
print("Enter / for division")
x=input("Enter a operator")
match x:
  case "+":
    print("Your answer is ",a+b)  
  case "-":
    print("Your answer is ",a-b)  
  case "/":
    print("Your answer is ",a/b)  
  case "*": 
    print("Your answer is ",a*b)  
    
      
    