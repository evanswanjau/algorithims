'''
A progrm that takes in the the number of candles in a birthday cake and the height of each
candle. Since the highest candle overshadows all the other candles the smaller candlescannot be blown out.
This program should print out the blown out candles.
'''

candles = input('Enter the number of candles on the cake: ')
height = input('Enter the heights if the respective candles - (seperated by a space) ')

def birthday_candles(candles, height):
    heights = height.split(' ') # Take out the space and set into a list
    heights = [int(i) for i in heights] # convert the string to integers

    max_value = max(heights)
    candles_blown = heights.count(max_value)

    print(candles_blown)

birthday_candles(candles, height)
