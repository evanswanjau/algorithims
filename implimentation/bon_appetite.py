'''
A program thet split a bill (in someways)
'''

values_and_constant = input("Enter number of values and constant: (seperate by space) ")
costs = input("Enter cost of items: (seperate by space) ")
charge = int(input("Enter amount to charge: "))

def string_to_list(the_list):

    the_list = the_list.split(' ') # Take out the space and set into a list
    the_list = [int(i) for i in the_list] # convert the string to integers

    return the_list

def bon_appetite(values_and_constant, costs):

    values_and_constant = string_to_list(values_and_constant)
    costs = string_to_list(costs)

    constant = values_and_constant[1]

    costs.pop(constant)

    total_cost = 0

    for i in costs:
        total_cost += i

    personal_cost = total_cost/2

    if charge <= personal_cost:
        print("Bon Appetite")
    else:
        print(int(charge - personal_cost))


bon_appetite(values_and_constant, costs)
