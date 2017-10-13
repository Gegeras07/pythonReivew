table = int(input('Choose a table: '))

ok = 0
nok = 0

#for x in range(10): #Começa em zero e vai até n-1
#for x in range(1,11): #Começa em n e vai até m-1
for x in range(2,10,2): #Começa em n e vai até m-1 com passo p
    answer = int(input("{0} X {1} = ".format(table, x)))
    if answer == x * table:
        print('Right!')
        ok += 1
    else:
        print("Wrong! {0} X {1} = {2}".format(table, x, x * table))
        nok += 1
    #print("{0} X {1} = {2}".format(table, x+1, (x+1)*table))
    
print("OK = {0}\nNOK = {1}".format(ok, nok))