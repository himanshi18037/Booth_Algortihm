
def _div(a, b):         # Main driver function

    # Error Handling
    if not (isinstance(a, int) or isinstance(b, int)):
        return 'Error: Enter a integer'
    
    if b == 0:
        return 'Error: Division by Zero is undefined'

    if abs(a) < abs(b):
        return 'Quotient: 0 0000\nRemainder: '+str(a)+' '+bin(a)[2:].zfill(4)

    #elif a == b:
     #   return 'Quotient: 1 0001\nRemainder: 0 0000'
        
    neg = False

    # Handling cases to convert negative number to their binary equivalent
    if a < 0 and b > 0:
        a = -1*a
        a_bin = bin(a)
        a_bin = comp2s(a_bin)
        b_bin = bin(b)
        neg = True

    elif b < 0 and a > 0:
        b = -1*b
        b_bin = bin(b)
        b_bin = comp2s(b_bin)
        a_bin = bin(a)
        neg = True

    elif a < 0 and b < 0:       # Handling case if both are negative
        a = -1*a
        b = -1*b
        a_bin = bin(a)
        b_bin = bin(b)
        a_bin = comp2s(a_bin)
        b_bin = comp2s(b_bin)

    else:
        a_bin = bin(a)      # converts a (dec) to binary equivalent
        b_bin = bin(b)      # converts b (dec) to binary equivalent

    a_len = len(a_bin) - 2  # calculates the length of binary number
    b_len = len(b_bin) - 2  # calculates the length of binary number

    # assigns the length of bits for calculation purposes in n (To decide the length of registers)
    n = a_len+1

    if a_len > b_len:
        n = a_len+1

    elif a_len < b_len:
        n = b_len+1

    # adding proper buffer of 0s
    
    M = bin(b)[2:].zfill(n+1)       # Divisor
    _M = comp2s(M)                  # Complement of divisor for subtraction
    A = bin(0)[2:].zfill(n+1)       # Accumulator (Remainder)
    Q = bin(a)[2:].zfill(n)         # Quotient
    buff = A+Q                      # for simultaneous shifting by 1

    # algorithm starts
    
    for i in range(n,-1,-1):        # Main Loop as described in flow chart

        # Final step
        if i == 0:
            break
        
        buff = shiftL(buff)     # shifts binary left by one
        A = buff[:n+1]
        Q = buff[n+1:]
        
        # 1st Step
        if A[0] == '0':
            A = _add(A,_M)      # adding 2's complement
            buff = A+Q

        elif A[0] == '1':
            A = _add(A,M)       # adding 2's complement
            buff = A+Q
        
        # 2nd Step
        if A[0] == '0':
            Q = Q[:-1]+'1'      # Deciding the last bit of Q
            buff = A+Q

        elif A[0] == '1':       # Deciding the last bit of Q
            Q = Q[:-1]+'0'
            buff = A+Q
    

    #if A[0] == '1':
     #   A = _add(A,M)

    #return 'Quotient: '+str(int(Q,2))+' '+Q+'\nRemainder: '+str(int(A,2))+' '+A
 
    if A[0] == '1' and not neg:     # Normalising Quotient
        A = _add(A,M)
        return 'Quotient: '+str(int(Q,2))+' '+Q+'\nRemainder: '+str(int(A,2))+' '+A

    elif A[0] == '1':               # If the binary of Quotient is negative then adding negative sign to decimal equivalent
        return 'Quotient: -'+str(int(Q,2))+' '+comp2s(Q)+'\nRemainder: '+str(int(_add(A,M),2))+' '+_add(A,M)

    elif neg:
        return 'Quotient: -'+str(int(Q,2))+' '+comp2s(Q)+'\nRemainder: '+str(int(A,2))+' '+A

    else:
        return 'Quotient: '+str(int(Q,2))+' '+Q+'\nRemainder: '+str(int(A,2))+' '+A       
            

# add two binary numbers (binary addition implementation)
def _add(a,b):

    res = ''        # stores the binary result
    carry = 0       # takeover carry for binary addition

    for i in range(len(a)-1,-1,-1):
        k = (int(a[i])+int(b[i])+carry)
        if k >= 2:                          # Carry 1 if 1+1 or 1+1+1(Previous Carry)
            carry = 1
        else:                               # Else make carry 0
            carry = 0
        res = str(k%2)+res

    return res

# 2's complement method implementation
def comp2s(a):

    l = len(a)
    c = bin(1)[2:].zfill(l)     # 1 to be added after 1's complement
    res = ''                    # storing result

    # Storing Result
    for i in a:
        if i == '0':
            res = res+str(1)

        else:
            res = res+str(0)

    return _add(res,c)

# Implements the Left Shift as existing Python shift operators don't allow for direct operations on binary
def shiftL(a):
    return a[1:]+'0'


