from cmath import inf

count = 0

largest_so_far = float("-inf")
second_largest_so_far = float("-inf")
smallest_so_far = float("+inf")

while count < inf:
    num = int(input("Give me a number: "))

    if num > largest_so_far:
        second_largest_so_far = largest_so_far
        largest_so_far = num

    if second_largest_so_far < num < largest_so_far:
        second_largest_so_far = num

    if num < smallest_so_far:
        smallest_so_far = num
    if count == 20:
        break
    count += 1

print("The largest number is ", largest_so_far)
print("The smallest number is: ", smallest_so_far)
print("The Second Largest value is:", second_largest_so_far)
