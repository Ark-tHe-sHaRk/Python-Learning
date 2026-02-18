# If statements let your program make decisions.
# Python checks if something is true, then runs the code under it.

age = int(input("How old are you? "))

# If the condition is true, this code runs.
if age >= 18:                             #If you are older than or equal to 18 the "if" code will run
    print("You are an adult.")
else:                                     #Anything else such as 13 or 2, the "else" code will run
    print("You are under 18.")

# You can also add more conditions using elif
grade = int(input("What grade did you get on your test? "))

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C.")
else:
    print("You need to study a bit more.")
