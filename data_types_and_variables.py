
###########################   Exercise 1  ################################
"""
takes dictionary that has movie title and amount of days rented.
"""
def calculate_total(a_dict):
    total = 0
    dollars_per_day = 3
    for movie, days in a_dict.items():
        product = days * dollars_per_day
        total += product
    return total

movies = {}
movies['little_mermaid'] = 3
movies['Brother Bear'] = 5
movies['Hercules'] = 1

# total is 27 dollars to pay to rent the movies
print(calculate_total(movies))


###########################   Exercise 2  ################################
"""
prompts user to input hours worked for each compnay, 
converts it to a total payment amount.
"""

def payment_for_work():
    # dollars per hour
    facebook_rate = 350
    google_rate = 400
    amazon_rate = 380

    # lets user input hours worked for each company
    fb_hours_worked = int(input("How many hours worked for facebook?"))
    google_hours_worked = int(input("How many hours worked for google?"))
    amazon_hours_worked = int(input("How many hours worked for Amazon?"))

    # Calculates payment amount from each company, creates total
    fb_pay = facebook_rate * fb_hours_worked
    google_pay = google_rate * google_hours_worked
    amazon_pay = amazon_rate * amazon_hours_worked
    total = fb_pay + google_pay + amazon_pay
    print("Total payment: $" + str(total))

    return total

#payment_for_work()

#ANSWER $7420


###########################   Exercise 3  ################################

"""
takes class information and student information, prints class availability for 
# each student 
"""
def student_scheduling(class_dict, student_dict):
    # for each student in the student info
    for students, student_info in student_dict.items():
            print("\n" + student_info['Student Name'] + ":\n")
            
            # for each class in the class info
            for classes, class_info in class_dict.items():
                if class_info['Class full']:
                    print(f"Class {class_info['Class Name']} unavailable due to being full.")
                
                # one if statement, checking student unavailability with class schedule
                elif any(conflicting_days in student_info['Student Unavailability'] \
                for conflicting_days in class_info['Class Schedule']):     
                    print(f"Class {class_info['Class Name']} is unavailable due to schedule conflict.")
                
                else:
                    print(f"Class {class_info['Class Name']} is available for registration")
            print()

# dictionary of class test info
class_dict = {
    'Class 1':
        {
            'Class Name': 'Algorithms',
            'Class Schedule': ['Mon', 'Wed', 'Fri'],
            'Class full': False
        },
    'Class 2':
        {
            'Class Name': 'Database Engineering 101',
            'Class Schedule': ['Tues', 'Thurs', 'Sat'],
            'Class full': False       
        },
    'Class 3':
        {
            'Class Name': 'Database Engineering 201',
            'Class Schedule': ['Tues', 'Thurs', 'Sat'],
            'Class full': True     
        }
}

# dictionary of student test info
student_info = {
    'Student 1':
    {
        'Student Name': 'Kyle Green',
        'Student Unavailability': ['Mon', 'Tues', 'Sun']
    },
    'Student 2':
    {
        'Student Name': 'Andrew Rachuig',
        'Student Unavailability': ['Sun']
    }
}

student_scheduling(class_dict, student_info)


###########################   Exercise 4  ################################
# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a 
# specific amount of products.

"""
checks member status, amount of products bought, and offer status to see if any
given customer can apply special product offers
"""

def can_apply_offer(customer_dict):
    if customer_dict['member status'] == 'Premium' and \
        customer_dict['offer status'] == 'active':
        print('\npremium member can apply offer\n')
        return True
    elif customer_dict['# of products bought'] > 2 and \
        customer_dict['offer status'] == 'active':
        print('\ncustomer bought enough items to apply offer\n')
        return False
    else:
        print('\noffer is no longer active\n')
        return False

customer_info1 = {
    'member status': 'Premium',
    '# of products bought': 1,
    'offer status': 'active'
}

customer_info2 = {
    'member status': 'normal',
    '# of products bought': 3,
    'offer status': 'active'
}

customer_info3 = {
    'member status': 'normal',
    '# of products bought': 3,
    'offer status': 'inactive'
}

can_apply_offer(customer_info1) # can apply
can_apply_offer(customer_info2) # can apply
can_apply_offer(customer_info3) # can not apply


###########################   Exercise 4  #################################
# Create a variable that holds a boolean value for each of the following conditions:

# - the password must be at least 5 characters
# - the username must be no more than 20 characters
# - the password must not be the same as the username
# - bonus neither the username or password can start or end with whitespace

"""
checks to see if there's whitespace at the beginning or end of a word/phrase.
Returns boolean, True = no leading/ending whitespace, False = there is whitespace.
"""
def no_whitespace(a_string):
    if a_string == a_string.strip(" "):
        return True
    else:
        return False


def input_username():
    satisfactory_username_flag = False
    while not satisfactory_username_flag:
        username = input("What would you like your username to be?\n" \
            "Requirements:\n " \
            " - Max of 20 characters\n " \
            " - No spaces in the beginning or end\n" \
            "Enter username: ")
        
        if len(username) < 1 or len(username) > 20 or not no_whitespace(username):
            print('Username does not meet requirements. Please enter a valid '\
                'username.\n\n')
        else:
            print('Username accepted.\n')
            satisfactory_username_flag = True
            return username


def input_password(username):
    satisfactory_password_flag = False
    while not satisfactory_password_flag:
        password = input("Enter a password.\n"\
            "Requirements:\n " \
            " - password can not be the same as username\n" \
            " - must not start or end with spaces\n" \
            " - password must be at least 5 characters\n" \
            "Enter password: ")

        if password == username or len(password) < 5 or not no_whitespace(password):
            print("\n\nPassword does not meet requirements. Please enter a valid " \
                "password.\n ")
        else:
            print("\n\nPassword accepted!")
            print(f"Username: {username}")
            print(f"Password: {password}\n\n")
            satisfactory_password_flag = True
            return password


def input_username_password():
    username = input_username()
    password = input_password(username)

    return [username, password]


input_username_password()