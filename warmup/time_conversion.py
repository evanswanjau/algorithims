'''
A program to convert timefrom 12hr clock system to 24 millitary system
'''

time = input('Enter time in the format(h:m:sAM/PM)')

def concatenateValue(int):

    int = str(int);

    if len(int) == 1:

        int = '0' + int


    return int




def time_conversion(time):

    value = time[-2]
    time = time[:-2]

    time = time.split(':') # Take out the space and set into a list
    time = [int(i) for i in time] # convert the string to integers

    h = time[0]
    m = time[1]
    s = time[2]

    if value == 'P':

        h += 12

        h = str(h)
        m = concatenateValue(m)
        s = concatenateValue(s)

        print(h + ":" + m + ":" + s)

    else:

        h = concatenateValue(h)
        m = concatenateValue(m)
        s = concatenateValue(s)

        print(h + ":" + m + ":" + s)



time_conversion(time)
