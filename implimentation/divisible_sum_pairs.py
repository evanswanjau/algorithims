'''
A program to find divisible sum pairs
'''

integers = input("Enter number of integers and constant respectively (seperate by spaces) ")
values = input("Enter the values (seperate by spaces) ")

def string_to_list(the_list):

    the_list = the_list.split(' ') # Take out the space and set into a list
    the_list = [int(i) for i in the_list] # convert the string to integers

    return the_list

def sum_pairs(integers, values):

    constant = string_to_list(integers)[1]
    values = string_to_list(values)

    count = 0
    i = 0

    while i < len(values)-1:

        if (values[i] + values[i+1]) % constant == 0:
            count +=1

        i += 1

    print(count)

sum_pairs(integers, values)
