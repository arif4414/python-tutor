# what is factorial .. if we pass 5 it should return 5*4*3*2*1
def factorial_calc():
    #x = int(input('pass factorial value '))
    x = 5
    f = 1

    for i in range(1, x+1):
        f = f*i
    return f


fac = factorial_calc()
print(fac)