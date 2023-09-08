
#add
def add(n1, n2):
  return n1 + n2
#subtract
def subtract(n1, n2):
  return n1 - n2
#multiply
def multiply(n1, n2):
  return n1 * n2
#divide
def divide(n1, n2):
  return n1 / n2

#Dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
num2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

should_continue = True

while should_continue:
  final_answer = answer
  
  continue_calculating = input(f"Type 'y' to continue calculating with {final_answer}, or type 'n' to exit: ").lower()
  
  if continue_calculating == 'n':
    should_continue = False
  else: 
    operation_symbol = input("Pick an operation: ")
    next_num = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(final_answer, next_num)
    final_answer1 = answer
    print(f"{final_answer} {operation_symbol} {next_num} = {final_answer1}")
  

  
  


