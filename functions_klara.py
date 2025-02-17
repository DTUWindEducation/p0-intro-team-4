# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:03:56 2025

@author: klara s204130
"""


#%% TASK 1

"""Define a function called greet that takes a name as a string, 
then prints "Hello, <name>!" to the screen.
"""

def greet(name):
    print(f'Hello, {name}!')

#greet('world')


#%% TASK 2

"""Goldilocks is 135 cm tall, and she is very picky about the size of 
her bed. If the bed is shorter than 140 cm, or larger than 150 cm, then 
she is unhappy. Write a function called goldilocks that takes the length 
of a bed in cm and prints whether goldilocks is happy with it. Be sure 
to distinguish whether the bed is too small or too large!"""

def goldilocks(length):
    if length > 150:
        print('Too large!')
    elif length < 140:
        print('Too short!')
    else:
        print('Just right. :)')


#goldilocks(139)
#goldilocks(140)
#goldilocks(151)
#goldilocks(150)


#%% TASK 3
"""Write a function called square_list that takes a list of numbers 
and returns a list where each element has been squared."""

def square_list(lst):
    list_squared=[]
    for i in lst:
        list_squared.append(i**2)
    return list_squared

#print(square_list([1,2,3]))


#%% TASK 4

"""Write a function called fibonacci_stop that returns a list of the 
Fibonacci numbers up to a specified maximum value. Recall that the 
Fibonacci sequence is a sequence in which the next number is the sum 
of the previous two numbers: 1, 1, 2, 3, 5, etc"""

def fibonacci_stop(max_value):
    fib_sequence = [1,1]
    value=1
    while value < max_value:
        value=fib_sequence[-1]+fib_sequence[-2]
        if value>max_value:
            break
        fib_sequence.append(value)
    return fib_sequence

#print(fibonacci_stop(60))

#%% TASK 5
"""
Instruments sometimes malfunction, returning incorrect values that 
can corrupt our analyses. Pretend we have an instrument that returns 
the pitch angle of a wind turbine blade, which usually ranges from 
0 to 90 degrees, but can report occasional values outside that range. 
The instrument also records a status signal, where 0 indicates that 
it is functioning normally but a positive value indicates some sort 
of malfunction. If a pitch angle is outside of [0, 90] degrees and 
the instrument is malfunctioning, we want to set the pitch angle to 
-999 to indicate a bad value. We ignore non-zero status signals if 
the pitch angle is in the correct range.


Define a function called clean_pitch that takes two lists, 
one representing measurements from the pitch instrument at certain 
points in time and the other representing the corresponding status 
signal. The function should return a cleaned list of the pitch angle, 
where “good” values are untouched and “bad” values are set to -999."""

def clean_pitch(x, status):
    cleaned = []
    for i in range(len(x)):
        if x[i]>90 and status[i]==1:
            cleaned.append(-999)
        elif x[i]<0 and status[i]==1:
            cleaned.append(-999)
        else: 
            cleaned.append(x[i])
    return cleaned

#x=[-1,2,3,95]
#status=[1,0,0,0]

#print(clean_pitch(x,status))


