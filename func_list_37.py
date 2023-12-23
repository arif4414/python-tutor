

def func_list(name):
    counter_fivePlus = 0
    counter_lessThanFive = 0

    for i in name:
        if len(i) > 5:
            counter_fivePlus = counter_fivePlus+1
        else:
            counter_lessThanFive = counter_lessThanFive+1
    return counter_fivePlus, counter_lessThanFive
    #print('names having more than 5 char ',counter_fivePlus)
    #print('names having <= 5 char ', counter_lessThanFive)

name = ['hafsah', 'rumaysa', 'arif', 'synthy', 'muaaz']
count1, count2 = func_list(name)
print('names having more than 5 char ',count1)
print('names having <= 5 char ', count2)
