'''
Created on 26-ene-2023

@author: Anton
'''

from java.util import ArrayList
from random import randint

if __name__ == '__main__':
    col = ArrayList()
    for i in range(10):
        col.add(i)
        
    print(col)
    print(type(col))
    
    L = list(col)
    print(L)
    
    L = [randint(1,100) for _ in range(10)]
    print(L)