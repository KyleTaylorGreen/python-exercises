from multiprocessing.sharedctypes import Value
import statistics


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]



# 1) How many students are there?

print(f"# of students: {len(students)}") # 14 students


# 2) How many students prefer light coffee? For each type of coffee roast?

coffee_pref = {}

for student in students:
    if student['coffee_preference'] not in coffee_pref:
        print(student["coffee_preference"])
        coffee_pref[student['coffee_preference']] = 1
    else:
        coffee_pref[student['coffee_preference']] += 1
print()

for roast_type in coffee_pref:
    print(f"{roast_type}: {coffee_pref[roast_type]}")
print()

#light: 3, medium: 6, dark: 5



# 3) How many types of each pet are there?

animal_species = {}

for student in students:
    for pet in student['pets']:
        if pet['species'] not in animal_species:
            print(pet['species'])
            animal_species[pet['species']] = 1
        else:
            animal_species[pet['species']] += 1
print()

for species in animal_species:
    print(f"{species}: {animal_species[species]}")
print()

# horse: 4  |   cat: 11   |   dog: 3

# 4) How many grades does each student have? Do they all have the same number of grades?


def first_grade_amnt():
    for student in students:
        return len(student['grades'])


def compare_grades(grade_amnt):
    if first_grade_amnt() != grade_amnt:
        return False
    else:
        return True

answer = True

for student in students:
    print(f"{student['student']}: {len(student['grades'])}")
    if not compare_grades(len(student['grades'])):
        answer = False

print(f'\nAll students have the same amount of grades: {answer}\n\n')


# 5) What is each student's grade average?


print("Average grade for each student: ")
for student in students:
    print(f"{student['student']}: {statistics.mean((student['grades']))}")


# 6) How many pets does each student have?

print("Number of pets for each student: ")
for student in students:
    print(f"{student['student']}: {len(student['pets'])}\n\n")


# 7) How many students are in web development? data science?

courses = {}

for student in students:
    if student['course'] not in courses:
        print(student["course"])
        courses[student['course']] = 1
    else:
        courses[student['course']] += 1
print()

for course_name in courses:
    print(f"{course_name}: {courses[course_name]}")
print()



# 8) What is the average number of pets for students in web development?
pet_count = 0
student_count = 0

for student in students:
    if student['course'] == 'web development':
        pet_count += len(student['pets'])
        student_count += 1

print(f"Avg # of pets per student in web dev: {pet_count/student_count}\n\n")


# 9) What is the average pet age for students in data science?

total_age = 0
pet_count = 0

for student in students:
    if student['course'] == 'data science':
        pet_count += len(student['pets'])
        for pet in student['pets']:
            total_age += pet['age']

avg_pet_age_data_science = round(total_age/pet_count, 2)

print(f"Avg age of pets of data science students: {avg_pet_age_data_science} years old\n\n")



# 10) What is most frequent coffee preference for data science students?


coffee_pref = {}

for student in students:
    if student['course'] == 'data science':
        if student['coffee_preference'] not in coffee_pref:
            print(student["coffee_preference"])
            coffee_pref[student['coffee_preference']] = 1
        else:
            coffee_pref[student['coffee_preference']] += 1
print()

highest_value = max(coffee_pref.values())


fav_flavor = [key for key, value in coffee_pref.items() if value == highest_value]
print(f"Favorite flavor(s) of Data Science students: {fav_flavor}\n")

# 11) What is the least frequent coffee preference for web development students?


coffee_pref = {}

for student in students:
    if student['course'] == 'web development':
        if student['coffee_preference'] not in coffee_pref:
            print(student["coffee_preference"])
            coffee_pref[student['coffee_preference']] = 1
        else:
            coffee_pref[student['coffee_preference']] += 1
print()

lowest_value = min(coffee_pref.values())

least_fav_flavor = [key for key, value in coffee_pref.items() if value == lowest_value]
print(f"Least favorite flavor(s) for web dev students: {least_fav_flavor}")


# 12) What is the average grade for students with at least 2 pets?
grade_total = 0
student_count = 0

for student in students:
    if len(student['pets']) >= 2:
        grade_total += statistics.mean(student['grades'])
        student_count += 1

average_grade = round(grade_total / student_count, 2)
print(f"\nAverage grade of students with 2 or more pets: {average_grade}\n")

# 13) How many students have 3 pets?

students_with_three_pets = len([student for student in students if len(student['pets']) == 3])
print(f"\n# of students with 3 pets: {students_with_three_pets}\n")


# 14) What is the average grade for students with 0 pets?


grades = [statistics.mean(student['grades']) for student in students \
          if len(student['pets']) == 0]

average_grade = round(statistics.mean(grades))
print(f"\nAverage grade of students with 0 pets: {average_grade}\n")


# 15) What is the average grade for web development students? data science students?


def average_grade_by_course(course_string):

    grades = [statistics.mean(student['grades']) for student in students \
              if student['course'] == course_string]

    average_grade = round(statistics.mean(grades))
    print(f"\nAverage grade of students in {course_string}: {average_grade}\n")

average_grade_by_course('web development') # 81.18
average_grade_by_course('data science') # 84.68



# 16) What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?


grade_ranges = [max(student['grades']) - min(student['grades']) \
                for student in students \
                if student['coffee_preference'] == 'dark']

average_grade_range_dark = round(statistics.mean(grade_ranges), 2)
print(f"\nAverage grade range for dark coffee drinkers: {average_grade_range_dark}\n")

# Answer: 28.8


# 17) What is the average number of pets for medium coffee drinkers?

pet_data = [len(student['pets']) for student in students \
            if student['coffee_preference'] == 'medium']

average_pet_for_medium_coffee = round(statistics.mean(pet_data), 2)
print(f"\nAverage # of pets for medium coffee drinkers: {average_pet_for_medium_coffee}\n")


# 18) What is the most common type of pet for web development students?

pet_dict = {}

for student in students:
    if student['course'] == 'web development':
        for pet in student['pets']:
            if pet['species'] not in pet_dict:
                pet_dict[pet['species']] = 1
            else:
                pet_dict[pet['species']] += 1


max_value = max(pet_dict.values())
most_common_pet = [key for key, value in pet_dict.items() if value == max_value]

print(f"\nMost common pet(s) for web dev students: {most_common_pet}\n")


# 19) What is the average name length?

total_length = 0

name_lengths = [len("".join(student['student'])) for student in students]
average_name_length = round(statistics.mean(name_lengths), 2)

print(f"\nAverage length of names: {average_name_length} letters\n")



# 20) What is the highest pet age for light coffee drinkers?

pet_ages_light_coffee_drinkers = [[pet['age'] for pet in student['pets']] \
                                for student in students \
                                if student['coffee_preference'] == 'light']

highest_age = max(max(pet_ages_light_coffee_drinkers))
print(f"\nHighest pet age for light cofffee drinkers: {highest_age} years old\n")


