try:
    print('Working.....')
    print('5'+5)


except Exception as e:
    print('There was a mistake here but I will continue the code.')

x=1
y=2

print(x+y)

#what this does is it says there is a mistake, but instead of making catastrophic failure and ending code
#it continues it to show the rest, without having to fix the rest of the code that is broken.

#there are differnet types of errors, Exception is a general allowance to any problem, which is good if there is a problem
#with the rest of the code, but nameerror, typeerror, are all specific allowances that help you find mistakes in typing

#you can also shorten it to do this

try:
    print('Running try...')
    print('5'+5)
except TypeError as t:
    print ('TypeError encountered')

