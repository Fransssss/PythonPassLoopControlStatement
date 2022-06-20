# pass = act as a placeholder

print("\nPass Loop Control Statement")
number = int(input("Input a limit number to count from zero: "))
numToPass = int(input("Input a number to pass/take out: "))

for i in range(1, number):           # start count from 1
    if i == numToPass:
        pass
    else:
        print(i)