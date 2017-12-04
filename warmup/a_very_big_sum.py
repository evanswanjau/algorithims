'''
program to print a list of items in an array added by the integer given as list length
then count given as power
'''
import math

value = int(input('Enter first integer: ')) # list length
count = int(input('Enter count: ')) # power
thelist = [] # store of our list


# function to add the integers together and append them to thelist
def big_sum(value, count):

	number = int(math.pow(10, count))
	highvalue = number + value

	# loop to append the list
	while number != highvalue:
		number = number + 1
		thelist.append(number)

	# loop to print out the numbers in the list
	for i in thelist:
		print(i)

big_sum(value, count) # call bug_sum
