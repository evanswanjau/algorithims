password = '4500'

num_count = 1
low_count = 1
upp_count = 1
sp_count = 1


numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

for i in password:

    if i in numbers:

        num_count = 0



    if i in lower_case:

        low_count = 0



    if i in upper_case:

        upp_count = 0


    if i in special_characters:

        sp_count = 0





pass_count = num_count + low_count + upp_count + sp_count

if len(password) < 6:

    len_count = 6 - len(password)


if len_count > pass_count:

    count = len_count

else:

    count = pass_count


print(count)
