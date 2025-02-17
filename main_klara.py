import numpy as np

print("Script started!")  # Debugging print

# Importing functions
from functions_klara import greet, goldilocks, square_list, fibonacci_stop, clean_pitch

print("Functions imported!")  # Debugging print

# Demonstrating functions
greet('WOOOOOOORLD')  # ✅ This should print

goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

print(square_list([1, 2, 3]))

print(square_list(np.array([4, 4, 4])))

print(fibonacci_stop(60))
print('test for fibonacci')
print(fibonacci_stop(30.5))
print('test for pitch')
print(clean_pitch(np.array([-7, 15, 35]), np.array([1, 1, 1])))


x = [-1, 2, 3, 95]
status = [1, 0, 0, 0]
print(clean_pitch(x, status))

print("Finished main script!")  # Debugging print

# Ensuring script execution only when run directly
if __name__ == '__main__':
    print("Running inside __name__ == '__main__'")  # Debugging print
    greet('WORRRRLD')  
    goldilocks(150)  
    print(square_list([4, 5, 6]))  
    print(fibonacci_stop(100))  
    print(clean_pitch([-5, 10, 30], [1, 1, 0]))  
