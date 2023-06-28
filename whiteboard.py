# The question asks the following: Write a function that takes an integer flight_length
#  (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean
#  indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

# Example input:
movie_lengths1=[20, 30, 110, 40, 50]
flight_length=160
# Example output:
True

# Example input:
movie_lengths2=[80, 110, 40]  #false
flight_length=160
# Example output:
False

def solution (flight_length, movie_lengths):
    myset=set()
    for i in movie_lengths:
        if flight_length-i in myset:
            return True
        myset.add(i)
    return False