def splitter(balance,avail_denom):
    
    denom_list = []
    word_list = [ j for i, j in avail_denom ]
    den_list = [ i for i, j in avail_denom ]
    
    for ele in den_list:
        loop_denom = int(balance/ele)
        remaining_balance = balance - loop_denom*ele
        denom_list.append(loop_denom)
        
        if(remaining_balance==0):
            break
        else:
            balance = remaining_balance
            pass
            
    return list(zip(denom_list,word_list))


def main():
    final_list=[]
    avail_denom = ((50,'Fifty'),(20,'Twenty') ,(10, 'Ten'),(5, 'Five'),(2,'Two'),(1,'One'),(.50,'Half Dollar'),(.25,'Quarter'),
        (.10,'Dime'),(.05,'Nickel'),(.01,'Penny'))
    print("Available Denominations: \n",avail_denom)
  
    PP = float(input('\nENTER PP:'))
    CH = float(input('\nENTER CH:'))

    if CH< PP:
        raise Exception("ERROR")
        
    elif CH== PP:
        print("ZERO")
        
    elif CH>PP :
        balance =  CH-PP;
        
        results = splitter(balance,avail_denom)
    
    for value,denom in results:
        if value !=0:
            for i in range(0,value):
                final_list.append(denom.upper())
    
    output = sorted(final_list)
    output = (',').join(output)
    print(" \n\nOUTPUT : ",output)

if __name__ == "__main__":
    main()
