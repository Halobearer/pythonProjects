variable = "Hello boss baby"
# for index, value in enumerate(variable):
# print(index)  # prints the index

for index, value in enumerate(variable):
    if value == "b":
        print(value, " : ", index)

for index, value in enumerate(variable):
    if value != "b":
        print(value, end="")
# print(value) # prints the value and the value is given as b
# print(index)  # prints the index: that is the numbers
# print(value, ":", index)
