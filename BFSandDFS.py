# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:26:22 2020

@author: Hp User
"""

close = []
opened = [] 
def getchild(b):
    print('Enter child of {0} , type 00 if no more child'.format(b))
    return input()

#####################################PART A###################################
def dfs_getter():
    while(input() != '00'):
        a = getchild(j)                     #keep getting child of j / nparent
        open.append(a)                      #consider the end of list, top of stack
    if(input() == '00' ):
        nparent = open.pop()                #if no more child, pop from TOS
        j = nparent                         # j will be new parent
        if nparent not in close:   
            close.append(nparent)           # nparent will be in closed 
        dfs_getter()                        #recursive unless pressed "quit"

####################################PART B####################################        
def bfs_getter():
    while(input() != '00'):
        a = getchild(j)                     #keep getting child of j / nparent
        open.append(a)                      #consider the end of list, top of stack
    if(input() == '00' ):
        nparent = open.popleft()            #if no more child, pop from head of queue
        j = nparent                         # j will be new parent
        if nparent not in close:
            close.append(nparent)           # nparent will be in closed 
        bfs_getter()                        #recursive unless pressed "quit"
        
k = input("enter bfs or dfs: ")        

def start():
    j = ''
    print('enter starting point: ')
    inp = input()  
    close.append(inp)
    getchild(inp)



if(k == 'dfs'):
    start()
    dfs_getter()
if(k == 'bfs'):
    start()
    bfs_getter()




    
        
    
    


