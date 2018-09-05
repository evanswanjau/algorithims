string = 'hackerrank'

check = 'hereiamstackerrank'

word = ''


for i in check:

    if i not in string:

        check = check.replace(i, '')


for i in string:

    for x in check:

        if i == x:

            word += x



if 'c' in check and 'e' in check and 'n' in check:

    print(check)

    print(check.index('c'), check.index('e'), check.index('n'))

    if check.index('c') < check.index('e') and check.index('c') < check.index('n') and check.index('e') < check.index('n'):

        for i in word:

            if word.count(i) > 1:

                if i == 'a' or i == 'k' or i == 'r':

                    if word.count('a') > 2:

                        word = word.replace('a', '', word.count(i) - 2)

                    elif word.count('k') > 2:

                        word = word.replace('k', '', word.count(i) - 2)

                    elif word.count('r') > 2:

                        word = word.replace('r', '', word.count(i) - 2)

                else:

                    word = word.replace(i, '', word.count(i) - 1)



        if len(string) == len(word):

            print('YES')

        else:

            print('NOs')

    else:

        print('NOd')

else:

    print('NOf')
