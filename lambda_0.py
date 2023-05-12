ls = [0,0,0,1,2,3,0] * 10

#print(ls)

#for customers in ls:
#    if customers >= 1:
#        print(customers)

iterator = filter(lambda customer: customer >= 1, ls)  # Doing the exactly same thing what above but on one line... 

for iteree in iterator:
    print(iteree)