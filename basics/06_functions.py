#Functions allow you to reuse code without repeating it
#You can define a function once and then call it whenever you need it 

#A simple function code
def greet():
  print("Hello! Welcome to my program!")

#Calling the function
greet()

#Making a function with a user input
def greet_person(name):
  print("Hello! ", name)

#A function that returns a value
def add_numbers(a, b):
  return a + b

result = add_numbers(3, 5)  
print("The result is", result)

#A function that returns a value after being a given a user input
def add(a, b):
  return(a+b)

#Asking the user for numbers
num1 = int(input("Give me your first number: "))
num2 = int(input("Give me your second number: "))

answer = add(num1 + num2)
print("The sum to your numbers are: ", answer)
