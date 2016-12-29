#while loops are just you saying 'while this is happening, do this'

condition = 1
while condition < 10:
    print (condition)
    condition += 1


'''
the plus equals just says, lets say, variable1, its saying variable 1 is variable 1 +1
'''

#lets say you do this

#condition1 = 5

#while condition1 <15
#    print ('true')

'''
be careful when you are defining the variable to NOT make it string, dont say condition1 = '5', because that is string
when you do the print ('true') you can also do this
'''

while True:
    print ('infinite')
'''
this will print infinite, infinitly, because 5 is always less than 5
I hashed out the first one because the while True statement will never start because the first one never ended
because its infinite
'''

#TIP: When running a program and its doing something out of control, just do cntrl+c to stop it.

# below is a infinite loop, just for fun
v = 3

if v < 4:
    print (v)