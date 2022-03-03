from art import logo

#calculator
print(logo)
#ADD
def add(n1,n2):
  return n1+n2
#substract
def substract(n1,n2):
  return n1-n2
#multiply
def multiply(n1,n2):
  return n1*n2
#divide
def divide(n1,n2):
  return n1/n2

#creating dictionary
operation={
  "+":add,
  "-":substract,
  "*":multiply,
  "/":divide
}
def calculator():
  num1 =int(input("Enter first number?: "))
  
  for symbol in operation:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    
    num2 =int(input("Enter Next number?: "))
    
    calculation_function= operation[operation_symbol]
    answer =calculation_function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y'to continue calculating with {answer},or type 'n'to exit: ")=="y":
      num1 = answer
    else:
      should_continue = False
  #calculator()


calculator()