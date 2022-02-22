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
print(end_zeros(10))

"""
You should return a given string in reverse order.
    Input: A string.
    Output: A string.
    Example:
        backward_string('val') == 'lav'
        backward_string('') == ''
        backward_string('ohho') == 'ohho'
        backward_string('123456789') == '987654321'
"""
def backward_string(val: str) -> str:
    # your code here
    val = str(val)
    return val[::-1]
print(backward_string("val"))

"""
You should write a function that will receive a positive integer and return:
    "Fizz Buzz" if the number is divisible by 3 and by 5;
    "Fizz" if the number is divisible by 3;
    "Buzz" if the number is divisible by 5;
    The number as a string for other cases.
    Input: A number as an integer.
    Output: The answer as a string.
    Example:
        checkio(15) == "Fizz Buzz"
        checkio(6) == "Fizz"
        checkio(5) == "Buzz"
        checkio(7) == "7"
    """
def checkio(number: int) -> str:
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.

    # replace this for solution
    number = int(number)
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 7 == 0:
        return str(number)
    return str(number)
print(checkio(15))

"""
In a given list the first element should become the last one. An empty list or list with only one element should stay the same.
    Input: List.
    Output: Iterable.
    Example:
        replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
        replace_first([1]) == [1]
"""
from typing import Iterable
def replace_first(items: list) -> Iterable:
    # your code here
    while True:
        if len(items) == 0:
            break
        else:
            num = int(items.pop(0))
            items.append(num)
            break
    return items
print(replace_first([1,2,3,4]))

"""
You have a number and you need to determine which digit in this number is the biggest.
    Input: A positive int.
    Output: An Int (0-9).
    Example:
        max_digit(0) == 0
        max_digit(52) == 5
        max_digit(634) == 6
        max_digit(1) == 1
        max_digit(10000) == 1
"""
def max_digit(number: int) -> int:
    # your code here
    numberStr = str(number)
    valueM = numberStr[0]
    for i in range(len(numberStr)):
        if int(numberStr[i]) > int(valueM):
            valueM = numberStr[i]
    return int(valueM)
print(max_digit(5279))

"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.
    Input: A string, that consist of digits.
    Output: An Int.
    Example:
        beginning_zeros('100') == 0
        beginning_zeros('001') == 2
        beginning_zeros('100100') == 0
        beginning_zeros('001001') == 2
        beginning_zeros('012345679') == 1
        beginning_zeros('0000') == 4
"""
def beginning_zeros(number: str) -> int:
    # your code here
    countZeros = 0
    for i in range(len(number)):
        if number[i] != "0":
            break
        elif number[i] == "0":
            countZeros += 1
    return int(countZeros)
print(beginning_zeros("0001000000"))

"""
You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.
    Let's look at a few examples:
        - array = [1, 2, 3, 4] and N = 2, then the result is 3 2 == 9;
        - array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.
    Input: Two arguments. An array as a list of integers and a number as a integer.
    Output: The result as an integer.
    Example:
        index_power([1, 2, 3, 4], 2) == 9
        index_power([1, 3, 10, 100], 3) == 1000000
        index_power([0, 1], 0) == 1
        index_power([1, 2], 3) == -1
"""
def index_power(array: list, n: int) -> int:
    """
        Find Nth power of the element with index N.
    """
    while True:
        if len(array) > n:
            number = array[n]
            return number ** n
        else:
            return -1
print(index_power([1,2],3))

"""
Find the nearest value to the given one.
You are given a list of values as set form and a value for which you need to find the nearest one.
    For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, and we need to find the nearest value to the number 9. If we sort this set in the ascending order, then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7, which means that the correct answer is 10.
    A few clarifications
        If 2 numbers are at the same distance, you need to choose the smallest one;
        The set of numbers is always non-empty, i.e. the size is >=1;
        The given value can be in this set, which means that it’s the answer;
        The set can contain both positive and negative numbers, but they are always integers;
        The set isn’t sorted and consists of unique numbers.
    Input: Two arguments. A list of values in the set form. The sought value is an int.
    Output: Int.
    Example:
        nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
        nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
"""
"""def nearest_value(values: set, one: int) -> int:
    # your code here
    if one == 0:
        for j in range(len(values)):
            one+=1
    for i in range(one):
        for value in values:
            if one == value or one - i == value or one + i == value:
                return value
print(nearest_value([4,7,10,11,12,17],0))"""