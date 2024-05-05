# num = int(input("Please input a number:\n"))
# print(type(num))

# if num % 3 == 0 and num % 5 == 0:
#     print("fizzbuzz\n")
# elif num % 3 == 0:
#     print("fizz\n")
# elif num % 5 == 0:
#     print("buzz\n")

for num in range(0, 20):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)