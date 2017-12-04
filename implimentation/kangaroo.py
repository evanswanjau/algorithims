'''
A program that tells whether two kangaroos moving in the same direction form diferrent starting points
and different velocities will ever meet at the same time
'''

location_and_velocity = input('Enter the location and rate of the two kangaroos (x1 v1 x2 v2)')

def meeting_point(location_and_velocity):

    location_and_velocity = location_and_velocity.split(' ') # Take out the space and set into a list
    location_and_velocity = [int(i) for i in location_and_velocity] # convert the string to integers

    move = 1

    while move == 1:
        location_and_velocity[0] += location_and_velocity[1]
        location_and_velocity[2] += location_and_velocity[3]

        print(location_and_velocity[0] , ' - ', location_and_velocity[2])

        if location_and_velocity[0] == location_and_velocity[2]:
            print('YES')
            break


meeting_point(location_and_velocity)
