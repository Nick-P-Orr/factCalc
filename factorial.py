import math

try:
    y = input('input factorial: ')
except SyntaxError:
    y = None

z = 1

'''
#range 2 to fact number
for i in range (1,y+1):
    z = z*i

print (z)
'''

'''
#without factorial function
def factCalc(fact, sum):
    sum = sum*fact
    fact = fact-1
    if (fact-1 != 0):
        factCalc(fact, sum)
    else:
        print(sum)

factCalc(y, z)
'''

#with factorial function, requires math import
def factCalc(fact):
    print math.factorial(fact)

factCalc(y)
