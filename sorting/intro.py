# function that finds the index of a value in a list

arr = [1, 4, 5, 7, 9, 12]

V = 4

def introTutorial(V, arr):

    count = 0

    while count < len(arr):

        if arr[count] == V:

            return count

        count += 1



print(introTutorial(V, arr))
