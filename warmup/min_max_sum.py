'''
program that taken in a string of numbers seperated by a space and getting the sum
of at least four of the numbers and returning the max and min of the numbers.
'''

string = input('Enter your string of numbers - (seperated by spaces)')

def min_max_sum(string):

    string = string.split(' ') # Take out the space and set into a list
    string = [int(i) for i in string] # convert the string to integers

    string_length = (len(string)) # string length for loop
    sum_array = [] # array to store total values

    i = -1
    while i < string_length - 1:
        i += 1
        value = string.pop(0)
        total = sum(string)
        sum_array.append(total)
        string.append(value)

    max_value = max(sum_array)
    min_value = min(sum_array)

    print(min_value, max_value)



min_max_sum(string)
