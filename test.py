# this file is to test methods/functions
import string

list1 = [("a", 1), ("b", 2), ("c", 3)]

print(list1[1][0])

for i in range(len(list1)):
    print(list1[i][0])


def return_string(a, b):
    string1 = a + b
    return string1


print(return_string("hey", "ho"))