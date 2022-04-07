
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
                    print("Class " + class_info['Class Name'] + " unavailable due to being full.")
                
                # one if statement, checking student unavailability with class schedule
                elif any(class_days in student_info['Student Unavailability'] \
                for class_days in class_info['Class Schedule']):     
                    print("Class " + class_info['Class Name'] + " is unavailable due to schedule conflict.")
                
                else:
                    print("Class " + class_info['Class Name'] + " is available for registration")
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