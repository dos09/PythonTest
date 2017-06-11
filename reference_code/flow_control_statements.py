# Flow control statements
#########################
rangelist = range(10)
print("rangelist: " + str(rangelist))
for number in rangelist: # must indent after ':'
    if(number == 1):
        continue
    elif(number != 5):
        print(number)
    else:
        break
print("end of 'for number in rangelist'")
for number in range(6, 8):
    print(number)
print("end of 'for number in range(6, 8)'")
for number in range(1,10,2): # range(from, to, step)
    print(number)
else: # comes here when no break is executed
    print("for loop ended normally without break")
print("end of 'for number in range(1,10,2)'")  
for number in range(1,3):
    pass # null/empty operation nothing is done
print("end of 'for number in range(1,3)'")  