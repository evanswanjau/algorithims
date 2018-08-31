'''

Function Description

--------------------------------------------------------------------------------

Complete the plusMinus function in the editor below. It should print out the ratio
 of positive, negative and zero items in the array, each on a separate line rounded
 to six decimals.

'''


# get number of rows and columns in the matrix array

def getLimit():

    n = int(input("Please enter array length: "));


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




def getArray():

    value = getLimit()

    count = 0

    integer_array = []


    while count < value:

        integer_array.append(int(input("Enter the desired value: ")))

        count += 1




    return integer_array







def plusMinus():

    arr = getArray()



    positive_count = 0

    negative_count = 0

    zero_count = 0



    for x in arr:

        if x > 0:

            positive_count += 1

        elif x == 0:

            negative_count += 1

        elif x < 0:

            zero_count += 1


    positive_fraction = '{0:.6f}'.format(positive_count / len(arr))

    negative_fraction = '{0:.6f}'.format(negative_count / len(arr))

    zero_fraction = '{0:.6f}'.format(zero_count / len(arr))


    print(positive_fraction)

    print(negative_fraction)

    print(zero_fraction)







plusMinus()
