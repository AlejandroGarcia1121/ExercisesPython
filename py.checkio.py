"""
This mission is the easiest one. Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.
    Input: Two arguments. Both are of type int.
    Output: Int.
    Example:
        mult_two(2, 3) == 6
        mult_two(1, 0) == 0
"""
def mult_two(a, b):
    # your code here
    return a * b
print(mult_two(2, 3))

"""
You have a positive integer. Try to find out how many digits it has?
    Input: A positive Int    
    Output: An Int.    
    Example:    
        number_length(10) == 2
        number_length(0) == 1
"""
def number_length(a: int) -> int:
    # your code here
    return len(str(a))
print(number_length(10))

"""
You are given a string and you have to find its first word.
    The input string consists of only English letters and spaces.
    There aren’t any spaces at the beginning and the end of the string.
    Input: A string.
    Output: A string.
    Example:
        first_word("Hello world") == "Hello"
    How it is used: The first word is a command in a command line.
    Precondition: The text can contain a-z, A-Z and spaces.
"""
def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    # your code here
    text = text.split(" ")
    return text[0]
print(first_word("Hello world"))

"""
Try to find out how many zeros a given number has at the end.
    Input: A positive Int
    Output: An Int.
    Example:
        end_zeros(0) == 1
        end_zeros(1) == 0
        end_zeros(10) == 1
        end_zeros(101) == 0
"""
def end_zeros(num: int) -> int:
    # your code here
    countZeros = 0
    index = -1
    for i in str(num):
        if str(num)[index] != "0":
            break
        elif str(num)[index] == "0":
            countZeros += 1
        index -= 1
    return countZeros
print(end_zeros(1))