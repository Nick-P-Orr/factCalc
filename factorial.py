try:
    y = input('input factorial: ')
except SyntaxError:
    y = None

z = 1

#range 2 to fibo number
for i in range (1,y+1):
    z = z*i

print (y, 'factorial equal to: ' ,z)
