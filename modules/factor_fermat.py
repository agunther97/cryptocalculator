from math import ceil, floor, sqrt

def factor_fermat(n):
    t=floor(sqrt(n)) #t is the square root of n, rounded down
    sq=pow(t,2)-n #calculate s
    while(t<n):
        if sqrt(sq)==floor(sqrt(sq)): #if it’s a perfect square
            break #stop looking
        else:
            t+=1 #check next t 
            sq=pow(t,2)-n #calculate s
    if sqrt(sq)==floor(sqrt(sq)): #if it’s a perfect square
        return [t,int(sqrt(sq))]
