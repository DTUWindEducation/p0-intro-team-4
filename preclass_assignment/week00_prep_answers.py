#Ex 1
def greet(name):
    print(f"Hello, {name}!")

greet("Vivi")



#Ex 2
def goldilocks(bed_length):
    if bed_length < 140:
        print("The bed is too small.")
    elif bed_length > 150:
        print("The bed is too large.")
    else:
        print("The bed is just right.")

goldilocks(138)


#Ex 3
def square_list(numbers):
    return [num**2 for num in numbers]

print(square_list([1,2,3]))


#Ex 4
def fibonacci_stop(n):
    if n<=0:
        return "The input needs to be a positive integer"
    elif n==1:
        return 0

    elif n==2:
        return 1
    else:
        return fibonacci_stop(n-1) + fibonacci_stop(n-2)
    
print (fibonacci_stop(10))


#Ex 5
def clean_pitch(pitch_measurements, status_signals):
    if len(pitch_measurements)!=len(status_signals):
        raise ValueError("Lists need to have the same length")

    cleaned_pitch=[
        pitch if (0<=pitch <=90 or status==0) else -999
        for pitch, status in zip(pitch_measurements, status_signals)
    ]
    return cleaned_pitch

#example
pitch_measurements=[10,15,100,87,200,34]
status_signals=[0,1,2,0,0,5]
cleaned_data=clean_pitch(pitch_measurements, status_signals)
print(cleaned_data)
