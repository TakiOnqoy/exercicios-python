import os
import string


# calculate the multiplication and sum of two numbers

def multiply_or_sum(num1, num2):
    if num1 * num2 > 1000:
        result = num1 + num2
    else:
        result = num1 * num2
    return result

# print(multiply_or_sum(int(input("Type the first number: ")), int(input("Type the second number: "))))

def sum_range_iteration():
    print("Printing current and previous number sum in a range(10)")
    previous_number = 0
    for i in range(10):
        print(f"Current number: {range(10)[i]} Previous number: {previous_number} Sum: {i + previous_number}")
        # if i >= 1:
            # previous_number += 1
        previous_number = i # one if less!

# sum_range_iteration()

# print only the even chars from any given string

def print_even_char():
    given_word = input("Type here any word to be printed: ")
    print("Printing only even index chars")
    # given_word_list = given_word.split() // o split divide o número de palavras, e não chars
    total_chars = len(given_word)
    for i in range(0, total_chars, 2):
        print(given_word[i])

#print_even_char()

# remove n first chars from a string

def remove_chars(word, n):
    word_output = '' # como ele será ele mesmo, precisa ser declarado antes
    for i in range (n, len(word), 1):
        word_output = word_output + word[i]
        print(word_output, word)
    print(word_output)

# remove_chars("cantico", 4)

def improved_remove_chars(s, n):
    return s[n:]

# print(improved_remove_chars("cantico", 4))

# check if first and last numbers in a list are equal

def compare_list_indexes(number_list):
    if number_list[0] == number_list[-1]:
        return True
    else:
        return False

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# print(comparing_list_indexes(numbers_y))

def display_multiples_five(number_list):
    print("Given list is", number_list)
    print("Divisible by five:")
    for i in range(len(number_list)):
        if number_list[i] % 5 == 0:
            print(number_list[i])

def display_multiples_five_2(number_list):
    print("Given list is", number_list)
    print("Divisible by five:")
    for num in number_list:
        if num % 5 == 0:
            print(num)

# numbers_z = [10, 20, 33, 46, 55]
# print(display_multiples_five(numbers_z))

# Count the number of occurrences of a string inside another string

def string_count(any_str, str_to_search):
    count = any_str.count(str_to_search)
    return count

# str_x = "Emma is good developer. Emma is a writer"
# word_x = "Emma"
# print(f"The number of times {word_x} appears on the string is {string_count(str_x, word_x)}")

def count_emma(statement):
    print("Given String:", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

# print("The number of occurrences of Emma is",count_emma("Emma is good developer. Emma is a writer"))

# print a sequence of numbers; number x should be printed x times

def print_numbers(num_list):
    for num in num_list:

        for i in range(num):
            print(num, end=' ')  # default end for print will be \n, but this can be changed as per the example
        print('') # this defines the shape

'''
        count = 0
        while count < num:
            print(num, end=' ')
            count += 1
'''


# list_x = [1, 2, 3, 4, 5]
# print_numbers(list_x)

# Check if string of numbers is a palindrome

def check_palindrome(num):
    num_str = str(num)
    list_str_num = list(num_str)
    reversed_list = list_str_num.copy()
    reversed_list.reverse()
    if list_str_num == reversed_list:
        return True
    else:
        return False
def improved_check_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# num = 586
# print(f"The number {num} is a palindrome? {improved_check_palindrome(num)}")

# Create a new list from two lists, containing the odd numbers from the first and even from the second

def create_new_list(list1, list2):
    new_list = []
    '''
    for num in list1:
        if list1[num] % 2 == 1: # erro aqui: eu estou tentando acessar o index quando ele já está com o valor direto da lista
            new_list.append(list1[i])
    '''
    for num in list1:
        if num % 2 == 1:
            new_list.append(num)
    for i in range(len(list2)):
        if list2[i] % 2 == 0:
            new_list.append(list2[i])
    return new_list

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print(f'The given lists were {list1} and {list2} and the resulting list is {create_new_list(list1, list2)}')

# Write a Program to extract each digit from an integer in the reverse order.

def reverse_digit_extraction(num):
    print("Given number", num)
    str_num = str(num)
    list_str_num = list(str_num)
    list_str_num.reverse()
    for num in list_str_num:
        print(num, end=' ')



def reverse_digit_extraction_modulo(num):
    print("Given number", num)
    while num > 0:
        # get the last digit
        digit = num % 10 # o resto de uma div por 10 é efetivamente o último algarismo dele, ou o retorno de % 10
        # remove the last digit and repeat the loop
        num = num // 10 # mesma lógica, mas aqui o retorno de // 10 é a div sem o resto, ou o alg com um alg a menos
        print(digit, end=" ")

# number = 7536
# reverse_digit_extraction_modulo(number)

# Calculate income tax for the given income by adhering to the below rules
# First $10,000 = 0%; Next $10,000 = 10%; Remaining = 20%

def tax_calculator(income):
    tax_due = 0
    if income > 20000:
        tax_range_0 = 10000
        tax_range_1 = 10000
        tax_range_3 = income - (tax_range_1 + tax_range_1)
        tax_due = tax_range_0 * 0 + tax_range_1 * 0.1 + tax_range_3 * 0.2
        return tax_due
    elif income > 10000:
        tax_range_0 = 10000
        tax_range_1 = income - tax_range_0
        tax_due = tax_range_0 * 0 + tax_range_1 * 0.1
        return tax_due
    else:
        tax_range_0 = income
        tax_due = tax_range_0 * 0
        return tax_due

# print(tax_calculator(10001))

# Print multiplication table from 1 to 10

def print_x_table(list):
    for i in range(10):
        for num in list:
            print(num * list[i], end=' ')
        print('')

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print_x_table(num_list)

# Print downward Half-Pyramid Pattern with asterisk

def print_downward_pyramid():
    for i in range(5, 0, -1):
        for j in range(i):
            print('*', end=' ')
            i += 1
        print('')

# print_downward_pyramid()

# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base, exp):
    def verify_positive_exp(exp):
        if exp >= 0:
            return True

    if verify_positive_exp(exp):
        result = base
        for i in range(1, exp):
            print("sthg")
            result = result * base
    return result

# print(exponent(2, 2))

# Accept numbers from a user

def num_input():
    def get_integer_input(num_prompt):
        while True:
            try:
                user_input = input(num_prompt)
                integer_value = int(user_input)
                return integer_value
            except ValueError:
                print("Invalid input. Please enter an integer.")
    num1 = get_integer_input("please, enter a number: ")
    num2 = get_integer_input("please, enter another number: ")
    result = num1 * num2
    return result

# print(num_input())

# Display three string “Name”, “Is”, “James” as “Name**Is**James”

# print("Name","is","James",sep='**')

# display a number in its octal version

def display_octal_num(num):
    print(f"The octal version of {num} is {num:o}")

# display_octal_num(54)

# Display float number with 2 decimal places using print
def display_float(num):
    print(f"{num:.2f}")

# display_float(458.541315)

# Accept a list of 5 float numbers as an input from the user

def float_list_from_input(input_prompt):
    float_input = input(input_prompt)
    float_list = float_input.split()
    for i in range(len(float_list)):
        float_list[i] = float(float_list[i])
    return float_list

def improved_float_list_from_input(input_prompt, list_size):
    float_list = []
    while len(float_list) < list_size:
        try:
            user_input = input(input_prompt)
            float_input = float(user_input)
            float_list.append(float_input)
        except ValueError:
            print("Invalid input. Please enter a valid float.")
    return float_list

def greatly_improved_float_list_from_input():
    n = int(input("Enter the size of list : "))
    print("\n")
    numList = list(map(float, input("Enter the list numbers separated by space ").strip().split()))[:n]
    print("User List: ", numList)

# good exercise but terrible code

# print(improved_float_list_from_input("Enter a list of 5 float numbers separated by spaces, following the pattern \"5.5\": ", 5))
# greatly_improved_float_list_from_input()

# Write all content of a given file into a new file by skipping line number 5

def create_file(file_name):
    print("Creating file",file_name)
    fp = open(file_name, 'w')
    fp.close()

def remove_file(file_name):
    os.remove('file_name')
    print(f"File {file_name} has been removed.")

def write_to_file(file_name, text_to_write):
    fp = open(file_name, 'r+')
    fp.writelines(text_to_write)
    fp.close()
    print(f"File {file_name} has been altered.")

def read_file(file_name):
    fp = open(file_name, 'r')
    file_content = fp.read()
    print(f"The file name is {file_name} and its content is:\n{file_content}")
    fp.close()
    return file_content

def copy_from_file(file_name1):
    fp = open(file_name1)
    content = fp.readlines()
    fp.close()
    return content
'''
source_file = "exemplo.txt"
destination_file = "test.txt"
text_to_write = "line1\nline2\nline3\nline4\nline5\nline6\nline7"

create_file(file_name)
write_to_file(file_name, text_to_write)
copy_from_file(file_name, "test.txt")
read_file(file_name)
read_file("test.txt")
'''
def exercise_five():

    with open(source_file, 'r') as fp:  # biggest reason for 'with' is automatic closure of file
        content = fp.readlines()
    with open(destination_file, 'w') as fp:
        count = 0
        for line in content:
            if count == 4:
                count += 1
                continue
            else:
                fp.write(line)
                count += 1
    read_file(destination_file)

# accept multiple strings from one input

def get_names():
    name1, name2, name3 = input("Enter the name of the three users separated by spaces: ").split()
    print(f"Name1: {name1}\nName2: {name2}\nName3: {name3}\n")

# get_names()

# check if a file is empty or not -- suggestion to use os.stat to get file size instead of content
def is_file_empty(file_name):
    with open(file_name) as fp:
        content = fp.read()
        if content == '':
            return True
        else:
            return False
# create_file("exemplo2.txt")
# file_name = "exemplo2.txt"
# print("Is the file", file_name, "empty?", is_file_empty(file_name))

# read line number 4

# content = copy_from_file("exemplo.txt")
# print(content[3])

# Print First 10 natural numbers using while loop
def print_natural_numbers():
    i = 1
    while i < 11:
        print(i)
        i += 1

def print_natural_numbers_for():
    for i in range(1, 11):
        print(i)

# print_natural_numbers_for()
# print_natural_numbers()

# Print the following pattern

def print_pyramid(total_rows):
    for i in range(1, total_rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print('')

# print_pyramid(5)

def sum_previous_numbers(limit_number):
    number_list = []
    for number_before in range(limit_number + 1):
        number_list.append(number_before)
    result = sum(number_list)
    return result
# print(sum_previous_numbers(10))

def improved_sum_previous_numbers(limit_number):
    sum_result = 0
    for i in range(limit_number + 1):
        sum_result += i
    return sum_result

def multiplication_table(number):
    for i in range(1, 11):
        print(number * i)

# multiplication_table(3)

def display_specific_numbers(list):
    for number in list:
        if number > 500:
            break
        elif number > 150:
            continue
        elif number % 5 == 0:
            print(number)
        else:
            continue

# display_specific_numbers([12, 75, 150, 180, 145, 525, 50])

def count_numbers_digits(number):
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    return count

# print(count_numbers_digits(1))

# print this upside down pyramid

def print_upside_down_pyramid(rows):
    for row in range(rows, 0, -1):
        for i in range(row, 0, -1):  # it doesn't reach zero because zero is the range limit, which is non-inclusive
            print(i, end=' ')
        print("")

# print_upside_down_pyramid(5)

# print this list in reversed order

def print_inverted_list(number_list):
    i = -1
    for i in range(0, len(number_list), 1):
        print(number_list[i])
        i = i - 1

def improved_print_inverted_list(number_list):
    for i in range(len(number_list) - 1, -1, -1):  # length returns one digit plus so it's human readable
        print(number_list[i])

def alternative_print_inverted_list(number_list):
    reversed_number_list = reversed(number_list)  # be careful with this syntax
    for number in reversed_number_list:
        print(number)

# improved_print_inverted_list([10, 20, 30, 40, 50])
# alternative_print_inverted_list([10, 20, 30, 40, 50])

def print_negative_numbers():
    for number in range(-10, 0, 1):  # it's inclusive on the starting digit, but it increments positively!
        print(number)

# print_negative_numbers()

# print done! after a successful for block

def else_for_block():
    for i in range(5):
        print(i)
    else:
        print("Done!")

# else_for_block()


def prime_numbers_within_range(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:  # bicho, INDENTAÇÃO. que doidera, o resultado fica totalmente diferente se nested under if.
                print(num)

# prime_numbers_within_range(25, 50)
'''
Proving that python has no problem converting a float to integer, which makes total sense
number = 4.58
number = int(number)
print(number)
'''
def fibonacci_sequence():
    sequence_list = []
    for i in range(10):
        if i == 0:
            next_number = 0
            sequence_list.append(next_number)
        elif i == 1:
            next_number = 1
            sequence_list.append(next_number)
        else:
            next_number = sequence_list[i - 1] + sequence_list[i - 2]
            sequence_list.append(next_number)
    return sequence_list

def alternative_fibonacci_sequence():
    num1 = 0
    num2 = 1
    for i in range(10):
        print(num1)
        res = num1 + num2
        num1 = num2
        num2 = res

# print(alternative_fibonacci_sequence())

def factorial(num):
    num_and_predecessors = []
    factorial = 1
    if num == 0:
        print("There's no fatorial for zero")
    for i in range(num, 0, -1):
        num_and_predecessors.append(i)
    for i in range(len(num_and_predecessors) - 1):
        factorial = num_and_predecessors[i] * factorial
    return factorial

def improved_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

# print(factorial(1))

# Reverse a given integer number

def reverse_integer_loop(num):
    inverted_number = ''
    while num > 0:
        remainder = num % 10
        num = num // 10
        inverted_number = inverted_number + str(remainder)
    return int(inverted_number)

def alternative_integer_loop(num):
    reverse_number = 0
    while num > 0:
        reminder = num % 10
        reverse_number = (reverse_number * 10) + reminder  # a more mathematical approach
        num = num // 10
    return reverse_number

# print(reverse_integer_loop(1234))

# Use a loop to display elements from a given list present at odd index positions

def display_odd_indexes(list):
    for i in range(1, len(list), 2):
        print(list[i])

# display_odd_indexes([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

def display_cube_numbers(num):
    for i in range(1, num + 1):
        index_cube = i * i
        print(f"The current number is {i} and its cube is {index_cube}")

# display_cube_numbers(6)

#  Find the sum of the series upto n terms

def sum_series_of_numbers(n):
    num_series_char = '2'
    temp = ''
    num_series_list = []
    for i in range(0, n):
        temp = temp + num_series_char
        num_series_list.append(temp)
    for i in range(len(num_series_list)):
        num_series_list[i] = int(num_series_list[i])
    return sum(num_series_list)

def improved_sum_series_of_numbers(n):
    starting_num = 2
    sum_nums = 0
    for i in range(n):
        sum_nums += starting_num
        starting_num = starting_num * 10 + 2
    return sum_nums

# print(improved_sum_series_of_numbers(5))

# Print a pyramid

def print_pyramid(rows):
    for i in range(rows):
        for j in range(i + 1):
            print('*', end=' ')
        print('')
    for i in range(rows - 1, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print('')

# print_pyramid(5)

def print_name_and_age(name, age):
    print(f'Hello there {name}, you are {age}!')

# print_name_and_age('Rafael Malaquias', 23)

def variable_arg_length(*args):
    print(f"Printing {len(args)} stored arguments:")
    for i in args:
        print(i)

# variable_arg_length(56, 'definition', 96, 83)

def calculation(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b, a - b
    else:
        print('Error: invalid argument values.')

# print(calculation(5, 4.5))

def show_employee(name, salary=9000):
    print(f"The employee's name is {name} and their salary is {salary}")

# show_employee('Jonas', 5600)

def inner_fuction_training(a, b):
    def args_sum(a, b):
        return a + b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return args_sum(a, b) + 5
    else:
        print('Invalid arg values.')

# print(inner_fuction_training(9, 5))

def recursive_function_training(limit):
    if limit:  # it will keep checking for truthy values
        return limit + recursive_function_training(limit - 1)
    else:
        return 0  # zero is considered a falsy value
# print(recursive_function_training(10))

def print_even_nums(start=4,end=30):
    for num in range(start + 1, end):
        if num % 2 == 0:
            print(num)

# print_even_nums()

def find_max_value(num_list):
    return max(num_list)

# print(find_max_value([4, 6, 8, 24, 12, 2]))

def create_new_string(str):
    starting_char = 0
    middle_char = len(str) // 2
    final_char = len(str) - 1
    return str[starting_char] + str[middle_char] + str[final_char]

# str = create_new_string('Jamesa')
# print(str)

def create_new_sliced_string(str):
    middle_char = len(str) // 2
    return str[middle_char - 1: middle_char + 2]  # again: start i is inclusive, final is exclusive

# print(create_new_sliced_string("JhonDipPeta"))

def append_str_to_mid(str, str2):
    str_mid = len(str) // 2
    new_str_init = str[0:str_mid]
    new_str_end = str[str_mid:len(str)]
    return new_str_init + str2 + new_str_end

# print(append_str_to_mid('Vanessa', 'Lloris'))

def new_string_craze(*strs):
    first_char = []
    mid_char = []
    last_char = []
    new_str = ''
    for i in range(len(strs)):
        first_char.append(strs[i][0])
        mid_char_i = len(strs[i]) // 2
        mid_char.append(strs[i][mid_char_i])
        last_char.append(strs[i][-1])
    for i in range(len(first_char)):
        new_str = new_str + first_char[i]
    for i in range(len(mid_char)):
        new_str = new_str + mid_char[i]
    for i in range(len(last_char)):
        new_str = new_str + last_char[i]
    return new_str

# print(new_string_craze('James', 'Potter', 'Hagrid'))

def rearrange_str_order(str):
    upper_str = ''
    lower_str = ''
    for i in range(len(str)):
        if str[i].islower():
            lower_str = lower_str + str[i]
        else:
            upper_str = upper_str + str[i]
    return upper_str + lower_str

# print(rearrange_str_order('JonAs'))

def check_number_of_types(str):
    char_list = []
    digit_list = []
    symbol_list = []
    for char in str:
        if char.isalpha():  # utilizado para checar se é char
            char_list.append(char)
        elif char.isdigit(): # utilizado para checar se é algarismo
            digit_list.append(char)
        else:
            symbol_list.append(char)
    return print(f'Number of characters in string is: {len(char_list)}\nNumber of digits in string is: {len(digit_list)}\
\nNumber of symbols in string is: {len(symbol_list)}')

# check_number_of_types("P@#yn26at^&i5ve")

def mix_two_strings(s1, s2):
    length = len(s1) if len(s1) > len(s2) else len(s2)
    reverse_s2 = s2[::-1]
    result = ''
    for i in range(length):
        if i < len(s1):
            result = result + s1[i]
        if i < len(s2):
            result = result + reverse_s2[i]
    return result

# print(mix_two_strings('Abc', 'Xyz'))

def check_balanced_strings(s1, s2):
    strings_are_balanced = True
    for char in s1:
        if char in s2:
            continue
        else:
            strings_are_balanced = False
            break
    return strings_are_balanced

# print(check_balanced_strings("Ynz", "PYnative"))

# Calculate the sum and average of the digits present in a string

def calc_sum_in_str(str):
    num_in_str = []
    for char in str:
        if char.isdigit():
            num_in_str.append(int(char))
    result = sum(num_in_str)/len(num_in_str)
    return result

# print(calc_sum_in_str("PYnative29@#8496"))

def count_char_occurences(str):
    char_dict = {}
    for char in str:
        char_dict[char] = str.count(char)  # a dict can't have two identical keys.
    return char_dict

# print(count_char_occurrences("apple"))

# print a given string in reverse

def print_reverse_str(str):
    rev_str = ''
    for i in range(len(str) - 1, -1, -1):
        rev_str = rev_str + str[i]
    return rev_str

# print(print_reverse_str('PyNative'))

def improved_print_reverse_str(str):
    str_rev_cp = str[::-1]
    return str_rev_cp

# print(improved_print_reverse_str('Pynative'))

def alternative_improved_print_reverse_str(str):
    str_rev_cp = ''.join(reversed(str))
    return str_rev_cp

# print(alternative_improved_print_reverse_str('Pynative'))

# Find the last position of a given substring

def substring_position(str):
    position = 0
    for i in range(len(str)):
        if str[i:i + 4] == 'Emma':
            position = i
    return f"last position of string 'Emma' started at index {position}"

def improved_substring_position(str, str_to_find):
    index = str.rfind(str_to_find)
    return f"Last position of substring {str_to_find} starts at index {index}"

# print(improved_substring_position("Emma is a data scientist who knows Python. Emma works at google.", 'Emma'))

def filter_list(str_list):  # list is a terrible name for a variable
    filtered_list = list(filter(None, str_list))  # iterates and takes out one value at a time
    return filtered_list

# print(filter_list(["Emma", "Jon", "", "Kelly", None, "Eric", ""]))

def transforming_string(any_str):
    new_str = any_str.translate(str.maketrans('Jon', 'Tom', string.punctuation))
    return new_str

# print(transforming_string("/*Jon is @developer & musician"))


# Create a list by picking an odd-index items from the first list and even index items from the second

def return_new_list(l1, l2):
    def is_valid_index(lst, index):
        return 0 <= index < len(lst)  # syntax checks these factor and return them as true or false

    l3 = []
    if isinstance(l1, list) and isinstance(l2, list):
        # length = len(l1) if len(l1) > len(l2) else len(l2)
        length = max(len(l1), len(l2))
        for i in range(length):
            if is_valid_index(l1, i) and i % 2 == 1:
                l3.append(l1[i])
            if is_valid_index(l2, i) and i % 2 == 0:
                l3.append(l2[i])
    return l3
'''
l1 = [3, 6, 9, 12, 15, 18, 21, 89, 78, 89, 74]
l2 = [4, 8, 12, 16, 20, 24, 28]
print(return_new_list(l1, l2))
'''

# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

def cutting_lists(list):
    cut_index = list.pop(4)
    print(f'List after removing element at index 4: {list}')
    list.insert(2, cut_index)
    print(f'List after adding element at index 2: {list}')
    list.append(cut_index)
    print(f'List after adding element at last index: {list}')

# cutting_lists([34, 54, 67, 89, 11, 43, 94])



