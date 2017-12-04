'''
Find most frequent bird (element)
'''
bird_count = int(input("Enter number of birds: "))
values = input("Enter bird types (seperate by spaces) ")

 # function fo convert string to list
def string_to_list(the_list):

    the_list = the_list.split(' ') # Take out the space and set into a list
    the_list = [int(i) for i in the_list] # convert the string to integers

    return the_list


def most_frequent_type(bird_count, values):

    values = string_to_list(values) # return list
    newdict = {} # store count
    newlist = [] # store dic values
    finallist = [] # store max values

    # add new values to dict
    for i in values:
        if i in newdict:
            newdict[i] += 1
        else:
            newdict[i] = 1

    # append the dict values to a new list
    for i in newdict:
        newlist.append(newdict[i])

    highest_value = max(newlist) # get highest_value in the count list

    # find the key with the highest value
    for i in newdict:
        if newdict[i] == highest_value:
            finallist.append(i) # append values to finallist incase of similarity


    print(min(finallist)) # find the min value in list


most_frequent_type(bird_count, values)
