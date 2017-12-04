'''
A program to convert timefrom 12hr clock system to 24 millitary system
'''

time = input('Enter time in the format(h:m:sAM/PM)')

def time_conversion(time):

    value = time[-2]
    time = time[:-2]

    time = time.split(':') # Take out the space and set into a list
    time = [int(i) for i in time] # convert the string to integers

    h = time[0]
    m = time[1]
    s = time[2]

    if value == 'P':
        print(h)
    else:
        print("0",h,":", m, ":", s, 'hrs')

time_conversion(time)
