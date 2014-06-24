import math
import random

def monte_carlo_method(tries,hits,num_itr,x,y,dist):
    num_itr = 30000
    tries = 0
    hits=0
    
    for i in range (0, num_itr):
        tries=tries + 1
        x=random.random(1,0)
        y=random.random(1,0)
        dist=(0.5*((x*x)+(y*y)))
        
        if dist <= 1:
            hits=hits+1
        else:
            hits=hits
                
    pi=4*(hits/tries)
   
  
    
            
            