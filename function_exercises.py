# 1) Define a function named is_two. It should accept one input and return True if 
# the passed input is either the number or the string 2, False otherwise.


'''
returns True if 2 or '2', false otherwise
'''
def is_two(two):
    # checks if 2 or '2', prints & returns true
    if two == 2 or two == '2':
        print('true\n')
        return True
    # prints/returns false if not 2 or '2'
    else:
        print('false\n')
        return False

# testing function by calling with 2 and '2' 
is_two(2)
is_two('2')




# 2) Define a function named is_vowel. It should return True if the passed string 
# is a vowel, False otherwise.


'''
returns true and prints if a vowel is passed, returns false/not a vowel if a consonant is passed
'''
def is_vowel(a_letter):
    # create list of vowels for comparison
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # converts any ints passed into a string so isalpha() can run properly
    a_letter = str(a_letter)


    #checks if passed value is a letter and if it's only one character
    if a_letter.isalpha() and len(a_letter) == 1:
        #checks if the letter is in the vowels list > if it's a vowel
        if a_letter.lower() in vowels:
            print('this is a vowel')
            return True
        else:
            print('not a vowel')
            return False
    # invalid input if the argument is not a single alpha char
    else:
        print('invalid input')
        return False
    print()

# testing the output to see if function works properly
is_vowel(3)   # invalid input
is_vowel('t') # not a vowel
is_vowel('e') # is a vowel
print()

# 3) Define a function named is_consonant. It should return True if the passed 
# string is a consonant, False otherwise. Use your is_vowel function to accomplish 
# this.


'''
uses previous is_vowel function to check if input is a vowel, and returns the opposite value > consonant
'''
def is_consonant(a_string):
    return not is_vowel(a_string)

# testing function output
print(is_consonant('t')) # not a vowel > true
print()



# 4) Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.


"""
accepts a string that is not a single character, uses previous is_consonant function to determine
if the word starts with a consonant and returns a capitalized version of the string if it is.
"""
def capitalize_word(a_word):
    # checks if argument is a string and is longer than a single character
    if type(a_word) == type(str()) and len(a_word) > 1:
        # checks if first letter of a_word is a consonant, returns capitalized word if true
        if is_consonant(a_word[0]):
            return a_word.capitalize()
        else:
            return a_word
    # invalid input if argument is not a string or string is only one char
    else:
        print('invalid input')


# testing function output
print(capitalize_word('hello')) # > Hello
print()



# 5) Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.


"""

"""
def calculate_tip(tip_percent, bill_total):
    # checks if tip percent is between 0 and 1
    if tip_percent >= 0 and tip_percent <= 1:
        # calculates & returns the tip amount based on bill_total and tip_percent
        total_tip = tip_percent * bill_total
        return total_tip

# testing/formatting function output with formatted string
print()
print(f"Total tip: ${calculate_tip(.15, 75)}")
print()



# 6) Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.


"""
calculates and returns the price after discount based on original price and discount percentage
"""
def apply_discount(original_price, discount_percentage):
    # calculates discount price, then returns it
    discount_price = original_price - (original_price * discount_percentage)
    return discount_price

# testing function output
print(f"Price after discount: {apply_discount(100, .75)}")
print()



# 7) Define a function named handle_commas. It should accept a string that is 
# a number that contains commas in it as input, and return a number as output.


"""
accepts string that's a number, returns number as int
"""
def handle_commas(number_string):
    # remove commas, convert string to int and return it
    number_string = int(number_string.replace(',', ""))
    return number_string

# testing function output
print(handle_commas('4,200')) # > 4200
print()



# 8) Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).


"""
accepts number and returns corresponding letter grade (A - F)
"""
def get_letter_grade(number_grade):
    if number_grade >= 90 and number_grade <= 100:
        return 'A'
    elif number_grade >= 80 and number_grade <= 89:
        return 'B'
    elif number_grade >= 70 and number_grade <= 79:
        return 'C'
    elif number_grade >= 65 and number_grade <= 69:
        return 'D'
    else:
        return 'F'

# testing function output
print()
print(get_letter_grade(80)) # --> B
print()



# 9) Define a function named remove_vowels that accepts a string and returns a 
# string with all the vowels removed.


"""
removes vowel from input string
"""
def remove_vowels(a_word):
    # creates list of vowels to compare against
    vowels = ['a', 'e', 'i', 'o', 'u']
    # empty string for adding letters made in list comprehension
    final_word = "" 
    # creates list of characters to add to string, join it to final_word
    final_word = final_word.join([letter for letter in a_word if letter not in vowels])
    
    return final_word

# testing output
print(remove_vowels("That's crazy"))  # -> Tht's crzy
print()



# 10) Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
#    - Name will become name
#    - First Name will become first_name
#    - % Completed will become completed

'''
takes input string and normalizes it based on the problem specifications
'''
def normalize_name(a_string):
    # creates list of characters if they are alpha, digit, or spaces
    final_word = ""
    final_word = final_word.join([letter.lower() for letter in a_string if letter.isdigit() \
                                  or letter.isalpha() or letter == " "])
    
    # strips leading/trailing whitespace, inserts underscores to replace spaces
    final_word = final_word.strip()
    final_word = final_word.replace(" ", "_")

    return final_word

print(normalize_name('Kyle'))        # -> kyle
print(normalize_name('Kyle Green'))  # -> kyle_green
print(normalize_name('% Completed')) # -> completed
print()



# 11) Write a function named cumulative_sum that accepts a list of numbers and
# returns a list that is the cumulative sum of the numbers in the list.


'''
accepts list of numbers and returns list that is a cumulative sum of numbers in the list passed
'''
def cumulative_sum(numbers):
    # empty list to hold cumulative sums
    cumulative_list = []
    for n in range(len(numbers)):
        # if n == 0 (first number), just append it
        if n == 0:
            cumulative_list.append(numbers[n])
        else:
        # append current number + previous number
            cumulative_list.append(numbers[n] + cumulative_list[n-1])
    
    # return list of cumulative sums
    return cumulative_list

print(cumulative_sum([1,1,1,])) # > [1, 2, 3]
print(cumulative_sum([1, 2, 3, 4])) # > [1, 3, 6, 10]


# Bonus 1) Create a function named twelveto24. It should accept a string in the 
# format 10:45am or 4:30pm and return a string that is the representation of the 
# time in a 24-hour format. Bonus write a function that does the opposite.

def twelveto24(time_string):
    
    # checks to see if p is in time for 'PM'
    pm_flag = False
    if 'p' in time_string.lower():
        pm_flag = True
    
    # create string of numbers from time string
    stripped_string =  ""
    stripped_string = stripped_string.join([num for num in time_string if num.isdigit()])
    
    # convert time string to int so we can do math
    time_num = int(stripped_string)
    
    # add 1200 and return time if pm flag is true, otherwise return the same time
    if pm_flag:
        time_num += 1200
        return str(time_num)
    else:
        return str(time_num)


# testing output
print()
print(twelveto24('4:30pm')) # -> 1630
print('\n')


# Bonus 2) Create a function named col_index. It should accept a spreadsheet column 
# name, and return the index number of the column.
#    - col_index('A') returns 1
#    - col_index('B') returns 2
#    - col_index('AA') returns 27


'''
accepts spreadsheet column and returns the index number of the column
'''
def col_index(column_label):
    # creates dictionary with the format {'A': 1, 'B': 2, 'C': 3, ...}
    # loop for every letter in the alphabet
    # turn string into number that can be incremented, turned back into a string
    # use resulting string as a key for alpha_index, set value to num + 1 (so 'A' == 1 instead of 'A' == 0, etc.) 
    alpha_index = {}
    for num in range(26):
        alpha_index[(chr(ord('A') + num))] = num + 1
    
    # reverses + capitalizes column label, "AB" -> "BA" so that column_label[0] == 'B', column_label[1] == 'A'
    # capitalized to match alpha_index keys

    column_label = column_label[::-1].upper()

    # the math/char conversion, set variable to hold index number sum of following loop.
    index_num = 0
    for x in range(len(column_label)):
        # column_lable[x] is the col label indexed by x from the range
        # --> our dict alpha_index[column_label[x]] is the number value of the letter(column_label[x])
        index_num += (alpha_index[column_label[x]] * 26 ** x)

        # equation: column_index = (Letter_number * 26 ** n) where n is place in label (one's place is 0, ten's place is 1, etc.)
        # EX: 700 = 7 * 10**2      |      70 = 7 * 10**1      |       7 = 7 * 10**0
        # --> 777 = (7 * 10**2)    +      (7 * 10**1)         +       (7 * 10**0)

        # A = 1, or (1 * 26 ** 0)        AB = 28, or ((1 * 26 ** 1) + (2 * 26 ** 0))
    
    # print and return index number
    print(f"column index of {column_label[::-1]}: {index_num}")
    return index_num

col_index('A') # 1
col_index('B') # 2
col_index('AA') # 27
col_index('AB') # 28
col_index('AZ') # 52
col_index('AAA') # 703
print(f"\nord A: {ord('A')}       ord B: {ord('B')}\n")


'''
returns index number for column label given. This function is ugly and a monstrosity made only to see how small I could get it. Maybe it's an ego thing.
¯\_(ツ)_/¯
'''
def col_index2(column_label):
    return sum([{chr(ord('A') + num): num + 1 for num in range(26)}[(column_label[::-1].upper())[x]] * 26 ** x for x in range(len(column_label))])
    

print(f"Column index of 'A': {col_index2('A')}") # 1
print(f"Column index of 'B': {col_index2('B')}") # 2
print(f"Column index of 'AA': {col_index2('AA')}") # 27
print(f"Column index of 'AB': {col_index2('AB')}") # 28
print(f"Column index of 'AZ': {col_index2('AZ')}") # 52
print(f"Column index of 'AAA': {col_index2('AAA')}") # 703
    