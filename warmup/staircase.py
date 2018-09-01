'''
program to look for create a staircase with similar base and height by the integer given
the last line must not have a space
'''

size = int(input("Please enter staircase length: "))

def adding_part(n):

    count = 0

    baseLength = []

    default_string = ''

    while count < n:

        i = 0

        value = (n - 1) - count

        default = ('{:^'+str(value)+'}').format(default_string)

        string = '#'

        while i < count:

            string += '#'

            i += 1


        print(default + string)

        count += 1




adding_part(size)
