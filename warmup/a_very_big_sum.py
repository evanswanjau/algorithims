'''
You are given an array of integers of size . You need to print the sum of the
elements in the array, keeping in mind that some of those integers may be quite
large.
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
