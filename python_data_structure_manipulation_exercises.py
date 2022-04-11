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

print(len(students)) # 14 students


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

print(f"Avg age of pets of data science students: {total_age/pet_count} years old\n\n")



# 10) What is most frequent coffee preference for data science students?
def first_coffee_flavor(coffee_info):
    for coffee_flavors in coffee_info:
        return coffee_flavors


coffee_pref = {}

for student in students:
    if student['course'] == 'data science':
        if student['coffee_preference'] not in coffee_pref:
            print(student["coffee_preference"])
            coffee_pref[student['coffee_preference']] = 1
        else:
            coffee_pref[student['coffee_preference']] += 1
print()

fav_coffee = [first_coffee_flavor(coffee_pref), coffee_pref[first_coffee_flavor(coffee_pref)]]


for pref in coffee_pref:
    print(f"{pref}: {coffee_pref[pref]}")
    if fav_coffee[1] < coffee_pref[pref]:
        fav_coffee = [pref, coffee_pref[pref]]
print(f'\nAnswer: {fav_coffee[0]}')


# 11) What is the least frequent coffee preference for web development students?




# 12) What is the average grade for students with at least 2 pets?
# 13) How many students have 3 pets?
# 14) What is the average grade for students with 0 pets?
# 15) What is the average grade for web development students? data science students?
# 16) What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# 17) What is the average number of pets for medium coffee drinkers?
# 18) What is the most common type of pet for web development students?
# 19) What is the average name length?
# 20) What is the highest pet age for light coffee drinkers?


