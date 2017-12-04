'''
program to look for create a staircase with similar base and height by the integer given
the last line must not have a space
'''

size = int(input("Please enter staircase length: "))

def adding_part(integer):
    count = 0
    baseLength = []

    while count < integer:
        count += 1
        baseLength.append('#')
        newLength = ''.join(baseLength)
        print(newLength)


adding_part(size)
