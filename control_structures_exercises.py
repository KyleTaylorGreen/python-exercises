############################## Exercise 1 ###############################
# a) prompt the user for a day of the week, print out whether the day 
#    is Monday or not

answer = input("Give a day of the week: ").lower()
if answer == 'monday':
    print('it is monday')
else:
    print("it's not monday")


# b) prompt the user for a day of the week, print out whether the day 
#    is a weekday or a weekend

weekends = ['saturday', 'sunday']
answer = input("Give a day of the week: ").lower()
if answer in weekends:
    print("It's a weekend day")
else:
    print("It's a weekday")


# c) create variables and make up values for
#     - the number of hours worked in one week
#     - the hourly rate
#     - how much the week's paycheck will be
#     - write the python code that calculates the weekly paycheck. 
#       You get paid time and a half if you work more than 40 hours

def calculate_paycheck(hours_worked, hourly_rate):
    overtime_hours = 0
    total_amount = 0
    
    if hours_worked <= 40:
        total_amount = hours_worked * hourly_rate
        return total_amount
    
    else:
        overtime_hours = hours_worked - 40
        overtime_amnt = overtime_hours * (hourly_rate * 1.5)
        total_amount = (40 * hourly_rate) + (overtime_amnt)
        return total_amount

print(calculate_paycheck(40, 10)) # 400 
print(calculate_paycheck(50, 10)) # 550



############################## Exercise 2 ###############################
# a) Create an integer variable i with a value of 5.

# b) Create a while loop that runs so long as i is less than or equal to 15

# c) Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

# d) Create a while loop that will count by 2's starting with 0 and ending 
#    at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

# e) Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

# f) Create a while loop that starts at 2, and displays the number squared 
#    on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 1000000:
    print(i)
    i = i ** 2

# g) Write a loop that uses print to create the output shown below.
# 100 - 5, steps of 5

i = 100
while i >= 5:
    print(i)
    i -= 5

########## FOR LOOOPS ###########

# h) Write some code that prompts the user for a number, then shows a 
#    multiplication table up through 10 for that number.
#    For example, if the user enters 7, your program should output:

answer = int(input("Please give me a number: \n\n"))
for num in range(1, 11):
    print(f"{answer} * {num} = {answer * num}")

# i) Create a for loop that uses print to create the output shown below
#    one 1, two 2's, three 3's, etc.

print() # formatting terminal output
for num in range(1, 10):
    print(f"{num}" * num)


# i) Prompt the user for an odd number between 1 and 50. Use a loop and a 
#    break statement to continue prompting the user if they enter invalid input. 
#    (Hint: use the isdigit method on strings to determine this). Use a loop 
#    and the continue statement to output all the odd numbers between 1 and 50, 
#    except for the number the user entered.
valid_answer = False

def check_number(number):
    if number % 2 != 0 and number > 1 and number < 50:
        return True
    else:
        return False

while not valid_answer:
    answer = input("Please give an odd number between 1 and 50: ")
    
    if answer.isdigit():
        answer = int(answer)
        
        if check_number(answer):
            valid_answer = True
            
            for num in range(1, 50):
                if num != answer and num % 2 != 0:
                    print(num)
                elif num == answer:
                    print(f'Skipping this number: {answer}')
        else:
            continue

# j) The input function can be used to prompt for input and use that input in your 
#    python code. Prompt the user to enter a positive number and write a loop that 
#    counts from 0 to that number. (Hints: first make sure that the value the user 
#    entered is a valid number, also note that the input function returns a string, 
#    so you'll need to convert this to a numeric type.)


while True:
    answer = input("please enter a positive number: ")
    if answer.lower() == 'exit':
        break
    if answer.isdigit():
        answer = int(answer)

        if answer > 0:
            for num in range(answer + 1):
                print(num)
            break
        else:
            continue
    else:
        continue

# k) Write a program that prompts the user for a positive integer. Next write a 
# loop that prints out the numbers from the number the user entered down to 1.


while True: 
    answer = input("please enter a positive integer: ")
    if answer.lower() == 'exit':
        break
    if answer.isdigit():
        answer = int(answer)

        if answer > 0:
            for num in range(answer, 0, -1):
                print(num)
            break
        else:
            continue
    else:
        continue

#################################### Exercise 3 ######################################
# 3) 
for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


#################################### Exercise 4 ######################################
# 4) Display a table of powers.
#    - Prompt the user to enter an integer.
#    - Display a table of squares and cubes from 1 to the value entered.
#    - Ask if the user wants to continue.
#    - Assume that the user will enter valid data.
#    - Only continue if the user agrees to.


while True: 
    answer = input("please enter a positive integer: ")
    if answer.lower() == 'exit':
        break
    if answer.isdigit():
        answer = int(answer)

        if answer > 0:
            print("\nnumber | square | cube \n"\
                  "-------|--------|-------".center(0))
            for num in range(1, answer + 1):
                print(f"{num}" + (" " * (7-len(str(num))))\
                    + "|" + f'{num ** 2}' + (" " * (8-len(str(num ** 2))))\
                    + "|" + f'{num ** 3}' + (" " * (8-len(str(num ** 3)))))
            wants_to_quit = input("would you like to quit? (y/n)").lower()
            if wants_to_quit == 'y' or wants_to_quit == 'yes':
                break
            else:
                continue

#################################### Exercise 5 ######################################

while True:
    answer = int(input("Please enter a numerical grade: "))
    if answer >= 88:
        print('A')
    elif answer <= 87 and answer >= 80:
        print('B')
    elif answer <= 79 and answer >= 67:
        print('C')
    elif answer <= 66 and answer >= 60:
        print('D')
    else:
        print('F')
    again = input('would you like to enter another grade? (y/n): ').lower()
    if again == 'y' or again == 'yes':
        continue
    else:
        break


#################################### Exercise 6 ######################################
# Create a list of dictionaries where each dictionary represents a book that you 
# have read. Each dictionary in the list should have the keys title, author, and genre.
# Loop through the list and print out information about each book.
# Prompt the user to enter a genre, then loop through your books list and 
# print out the titles of all the books in that genre.

list_of_books = [
    {
        'title': 'Frankenstein',
        'author': 'Mary Shelley',
        'genre': 'science fiction'
    },
    {
        'title': "Hitchhiker's Guide to the Galaxy",
        'author': 'Douglas Adams',
        'genre': 'science fiction'
    },
    {
        'title': 'A Confederacy of Dunces',
        'author': 'John Kennedy Toole',
        'genre': 'comedy'
    }
]

genres = []
for books in list_of_books:
    #print(books.keys())
    print(f"\nTitle: {books['title']}")
    print(f"Author: {books['author']}")
    print(f"Genre: {books['genre']}\n")
    genres.append(books['genre'])


user_genre = input("Which genre of books would you like to see? ")
if user_genre in genres:
    for books in list_of_books:
        if books['genre'] == user_genre:
            print(f"\nTitle: {books['title']}")
            print(f"Author: {books['author']}")
            print(f"Genre: {books['genre']}\n")
else:
    print("\nSorry, we don't have that genre of book!")