 # Program that shares chocolate

chocolate_bars = int(input('Enter number of chocolate bars: '))
values = input('Enter chocolate bar values (seperate by space) ')
day_and_month = input('Enter day and month respectively (seperate by space) ')

def string_to_list(the_list):

    the_list = the_list.split(' ') # Take out the space and set into a list
    the_list = [int(i) for i in the_list] # convert the string to integers

    return the_list

def chocolate_sharing(chocolate_bars, values, day_and_month):

    values = string_to_list(values)
    day_and_month = string_to_list(day_and_month)
    values_length = len(values)

    day = day_and_month[0] # value of day
    month = day_and_month[1] # value of month

    sum_of_values = 0
    count = 0
    start_point = 0
    c = -1

    while c < values_length:
        c += 1

        if sum(values[c:month]) == day:
            count += 1

        month += 1


    print('count', count)


chocolate_sharing(chocolate_bars, values, day_and_month)
