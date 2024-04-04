name = input("please enter your name: ")
password = input("please enter your password: ")
repeat_password = input("please enter your password again: ")
if password == repeat_password:
    print(name, "registered succesfully")
else:
    print("invalid input")
    