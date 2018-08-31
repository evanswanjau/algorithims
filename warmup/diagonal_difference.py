'''

Function description

--------------------------------------------------------------------------------

Complete the digonal differencc function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:

arr: an array of integers.

#link: https://www.hackerrank.com/challenges/diagonal-difference/problem

'''

import math


# get number of rows and columns in the matrix array

def getLimit():

    n = int(input("Please enter rows and columns array length: "));


    # ensure that it is greater than -100 and less that 100

    if n < -100:

        print('Your value cannot be less than -100')

        value = int(input("Please enter rows and columns array length: "))

    elif n > 100:

        print('Your value cannot be greater that 100')

        value = int(input("Please enter rows and columns array length: "))

    else:

        value = n


    return value;




def getIntegers():

    value = getLimit()

    i = 0

    integers_array = []

    while i < value:

        count = 0

        integer_array = []


        while count < value:

            integer_array.append(int(input("Please enter the desired values")))

            count += 1

        integers_array.append(integer_array)

        print('\nEnter values for the next array\n')

        i += 1






    return integers_array




def getDifference():

    integers_array = getIntegers()

    count = 0

    primary_diagonal_sum = 0

    secondary_diagonal_sum = 0



    while count < len(integers_array):

        primary_diagonal_sum += integers_array[count][count]

        secondary_diagonal_sum += integers_array[count][len(integers_array) - (count + 1)]

        count += 1



    difference = abs(primary_diagonal_sum - secondary_diagonal_sum)


    print(difference)






getDifference()
