string = input("Enter string: ")

def reduce_string(string):

    word_list = []

    for i in string:
        count = string.count(i)
        string = string.replace(i, '')

        print(string)



reduce_string(string)
