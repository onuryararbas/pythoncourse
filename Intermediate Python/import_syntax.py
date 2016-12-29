import statistics as s
#What i did here was shorten statistics to s, so I dont have to type out statistics every time I want to call it
List = [1,2,3,4,5,6,7,8,9]

print(s.mean(List))

#This is what you could also do
from statistics import mean as m

print(m(List))

#same answer, but solved in a shorter amount of code

#you can also do this

from statistics import mean as m, stdev as s

print(m(List))
print(s(List))
#now you found the standard deviation
#If you hadn't made the code shorter by putting the functions into single letters, it would look like

from statistics import mean
from statistics import stdev

print(mean(List))
print(stdev(List))

# and not to mention the fact that the list from above needs to be there, the code is a lot more elongated
#than it could be