# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 22:57:16 2018

@author: Chen
"""
def choice(m,n):
    if n==1:
        return m.count('w')
    else:
        s=0
        for i in range(len(m)):
            w=m[:]
            if w[i]=='w':
                w[i]='b'
            else:
                w[i]='w'

            s+=choice(w,n-1)
        return s

def pow_(a,b):
    c=1
    while b>0:
        c*=a
        b-=1
    return c
    
def probability(marbles, step):
    m=[]
    for i in marbles:
        m.append(i)
    l=len(m)
    n=step

    a=choice(m,n)
    b=pow_(l,n)
    
    return float('%.3f'%(a/b))


if __name__=='__main__':
    print(probability('bbw', 2))
    print(probability('bwbwbwb', 5))