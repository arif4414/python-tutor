
print('DB connection open')
try:
    a = 6
    b = 0
    print(a/b)
except ZeroDivisionError as e:
    print('please provide valid value for divisor')

try:
    k = int(input('enter a number'))
    print(k)
except ValueError as e:
    print('please provide a number')

except Exception as e:
    print('something else went wrong', e)

finally:
    print('DB connection closed')