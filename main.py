import art

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

print(art.logo)

dict = {"+": add,
        "-": sub, 
        "*": mul, 
        "/": div,
        "":""}

result = float(input("What's the first number: "))
operation = ""

while operation != "n":
  if(operation in dict):
    num1 = result
  
    if operation == "":
      for o in dict:
        print(o)
      operation = input("Pick an operation from the line above: ")
    
    num2 = float(input("What's the next number: "))
  
    result = dict[operation[0]](num1, num2)
    
    print(f"{num1} {operation} {num2} = {result}")
    
  operation = input(f"Type the new operation to continue calculating with {result}, or type 'n' to exit: ")