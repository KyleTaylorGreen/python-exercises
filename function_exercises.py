# 1) Define a function named is_two. It should accept one input and return True if 
# the passed input is either the number or the string 2, False otherwise.

def is_two(two):
    if two == 2 or two == '2':
        print('true\n')
        return True
    else:
        print('false\n')
        return False
    
is_two(2)
is_two('2')

# 2) Define a function named is_vowel. It should return True if the passed string 
# is a vowel, False otherwise.

def is_vowel(a_letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    a_letter = str(a_letter)
    if a_letter.isalpha() and len(a_letter) == 1:
        if a_letter.lower() in vowels:
            print('this is a vowel')
            return True
        else:
            print('not a vowel')
            return False
    else:
        print('invalid input')
        return False
    print()

is_vowel(3)
is_vowel('t')
is_vowel('e')
print()

# 3) Define a function named is_consonant. It should return True if the passed 
# string is a consonant, False otherwise. Use your is_vowel function to accomplish 
# this.


def is_consonant(a_string):
    return not is_vowel(a_string)

print(is_consonant('t'))


# 4) Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.

def capitalize_word(a_word):
    if is_consonant(a_word[0]):
        return a_word.capitalize()
    else:
        return a_word

print(capitalize_word('hello'))

# 5) Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percent, bill_total):
    total_tip = tip_percent * bill_total
    return total_tip
print()
print(f"Total tip: ${calculate_tip(.15, 75)}")
print()

# 6) Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    discount_price = original_price - (original_price * discount_percentage)
    return discount_price

print(apply_discount(100, .75))
print()

# 7) Define a function named handle_commas. It should accept a string that is 
# a number that contains commas in it as input, and return a number as output.

def handle_commas(number_string):
    number_string = int(number_string.replace(',', ""))
    return number_string

print(handle_commas('4,200'))
print()

# 8) Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).

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

print()
print(get_letter_grade(80))
print()

# 9) Define a function named remove_vowels that accepts a string and returns a 
# string with all the vowels removed.

def remove_vowels(a_word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    final_word = ""
    final_letters = [letter for letter in a_word if letter not in vowels]
    for letter in final_letters:
        final_word += letter
    return final_word

print(remove_vowels("That's crazy"))
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


def normalize_name(a_string):
    final_letters = [letter.lower() for letter in a_string if letter.isdigit() or letter.isalpha() or letter == " "]
    final_word = ""
    for letter in final_letters:
        final_word += letter

    #print(final_word)
    final_word = final_word.strip()
    final_word = final_word.replace(" ", "_")

    return final_word

print(normalize_name('Kyle'))
print(normalize_name('Kyle Green'))
print(normalize_name('% Completed'))

# 11) Write a function named cumulative_sum that accepts a list of numbers and
# returns a list that is the cumulative sum of the numbers in the list.

def cumulative_sum(numbers):
    cumulative_list = []
    for n in range(len(numbers)):
        if n == 0:
            cumulative_list.append(numbers[n])
        else:
            cumulative_list.append(numbers[n] + cumulative_list[n-1])
    
    return cumulative_list

print(cumulative_sum([1,1,1,])) # > [1, 2, 3]
print(cumulative_sum([1, 2, 3, 4])) # > []