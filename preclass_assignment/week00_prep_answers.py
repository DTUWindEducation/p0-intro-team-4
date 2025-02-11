#Exercise 1 - Creat Function
def greet():
   print("Hello World!")                  #print in a function
greet()

#Exercise 2 - If/else statements

def goldilocks(X):                        #Usage of if function to differenciate the 3 cases Too small, right, too big
    if X < 140:
        return "Too small!"
    elif X >= 140 and X <= 150:
        return "Just right. :)"
    else:
        return "Too large!"

bed_size = 139
print("Decition Goldilocks: ", goldilocks(bed_size))


#Exercise 3 - Square List
def square_list(list):                    #Function to square each element of a list
    list_sq = [x**2 for x in list]        
    return list_sq

list = [1, 2, 3]
print("Original list: ", list)
print("Squared list: ", square_list(list))

#Exercise 4 - Fibonacci List
list_fib = [1, 1]       #Create Beginnerlist
def fibonacci_stop(X):
    i = 1
    while i < X:            #while loop 
        i = list_fib[-1] + list_fib[-2]
        if i == 34:                         #Break before inserting first Fibonacci number out of bounds
            break
        list_fib.append(i)
    return list_fib

Number_Stop_Fibonacci = 30                  #Definition number to stop Fibonacci series
print("Fibonacci series untill break point: ", fibonacci_stop(Number_Stop_Fibonacci))


# Exercise 5 - Logical operator 
raw_pi = [-1, 2, 6, 95]  # List with "raw" pitch angle
status = [1, 0, 0, 1]  # List with status signal

def clean_pitch(raw_pi, status):
    for X in range(len(raw_pi)):            #checking elements of List raw_pi
        if raw_pi[X]<0 or raw_pi[X]>90:     #checking conditions with if functions 
            if status[X] == 1:
                raw_pi[X] = -999
            else:
                pass
        else:
            pass
    return raw_pi

print("Corrected list of pitch angels: ", clean_pitch(raw_pi, status))