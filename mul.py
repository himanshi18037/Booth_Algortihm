
def mul(a, b):         # Main driver function

    # Error Handling
    if not (isinstance(a, int) or isinstance(b, int)):
        return 'Error: Enter a integer'
    
    if a==0 or b==0:
        # print(0)       #if either of the number is 0
        return 'Product is 0'
        
    nega=True
    if(a<0):
        a=-1*a
        nega = False

    negb=True
    if(b<0):
        b=-1*b
        negb= False

    a_bin=bin(a)[2:]
    b_bin=bin(b)[2:]
    a_len=len(a_bin)
    b_len=len(b_bin)

    # assigns the length of bits for calculation purposes in n (To decide the length of registers)
    n = 0
    count=0;
    if a > b :
        n = a_len+2
        count=b_len

    else: 
        n = b_len+2
        count=a_len

    # adding proper buffer of 0s
    
    M = '0'*(n-a_len)+bin(a)[2:]      
    _M = comp2s(M)
    if(nega==False):
        M,_M=_M,M
    B = '0'*(n-b_len)+bin(b)[2:]     
    _B = comp2s(B) 
    if(negb==False):
        B,_B=_B,B                
    A = '0'*(n)      # Accumulator(for storing the intermediate results)
    Q = '0'         
   

    finallist=[]
    x=''
    for i in range(n,-1,-1):        # Main Loop as described in flow chart
        templist=[]
        
        if i == 0:
           break;
            
       
        if(str(B[-1])+str(Q)=='11' or str(B[-1])+str(Q)=='00'):
            temp=str(A)+str(B)+str(Q)
            temp=shiftR(temp)
            A=str(temp[0:len(A)])
            B=str(temp[len(A):-1])
            Q=str(temp[-1])
            templist=[A,B,Q]
            finallist.append(templist)

        elif(str(B[-1])+str(Q)=='10'):
           A=_add(A,_M,n)
           temp=str(A)+str(B)+str(Q)
           temp=shiftR(temp)
           A=str(temp[0:len(A)])
           B=str(temp[len(A):-1])
           Q=str(temp[-1])
           templist=[A,B,Q]
           finallist.append(templist)
           

        elif(str(B[-1])+str(Q)=='01'):
           A=_add(A,M,n)     
           temp=str(A)+str(B)+str(Q)
           temp=shiftR(temp)
           # print(temp)
           A=str(temp[0:len(A)])
           B=str(temp[len(A):-1])
           Q=str(temp[-1])
           templist=[A,B,Q]
           finallist.append(templist)

    x=str(A)+str(B)
    return "Binary Product: "+x+' '+'\nDecimal Product: '+str(binconversion(x))





# def toprint(a){
#    print("Accum:","\t","B0","\t","Q")
#    print("----------------------")
#    for i in finallist:
#       print(i[0],"\t",i[1],"\t",i[2])
#       print("---------------------") 
# }           

# add two binary numbers (binary addition implementation)
def _add(a,b,n):

    deca=int(a,2)
    decb=int(b,2)
    temp=deca+decb
    final=bin(temp)[2:]
    lenf=len(final)
    final='0'*(n-lenf)+final
    if(len(final)>n):
        return final[len(final)-n:]

    
    return final

#flip method for Two's Complement Implementation
def flip(aa):
    aa=list(aa)
    for i in range(len(aa)):
        if(str(aa[i])=='0'):
            aa[i]='1'
        else:
            aa[i]='0'
    temp=''
    for i in aa:
        temp=temp+i
    return temp

# 2's complement method implementation
def comp2s(aa):
    l = len(aa)
    c = bin(1)[2:].zfill(l-1)     # 1 to be added after 1's complement
    result=_add(flip(aa),c,l)
    return result

def shiftR(aa):
    return str(aa[0])+str(aa[:-1])
  
# method two convert 
def binconversion(aa):
    if(aa[0]=='1'):
        return int(comp2s(aa),2)*-1
    else:
        return int(aa,2)



# print(binconversion(c))