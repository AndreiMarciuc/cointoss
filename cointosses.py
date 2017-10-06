def coinTosses(reps):
    tail=0
    head=0
    
    for i in range (1,reps):
        temp=i
        import random
        random_num=random.randint(0,1)
        i=random_num
        if i==0:
            tail=tail+1
            
            print "Atempt #",temp,":Throwing a coin...It's tail ! Got",tail,"tail(s) so far and ",head,"head's so far"
        elif i==1:
            head=head+1
           
            print "Atempt #",temp,":Throwing a coin...It's a head ! Got",tail,"tail(s) so far and ",head,"head's so far"
            
coinTosses(10)