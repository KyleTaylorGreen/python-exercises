#from function_exercises import calculate_tip as ct, handle_dollar_sign_commas
import function_exercises
import itertools
import json


# 1 b) Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly.
#  Call this function with values you choose and print the result.
print(function_exercises.calculate_tip(.04, 100))

# 2 a) How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

print(f"Different ways you can combine 'abc' and [1,2,3]: {len(list(itertools.product('abc', [1,2,3])))}")

# b) How many different combinations are there of 2 letters from "abcd"?

print(f"Combination of 2 letters from 'abcd': {len(list(itertools.combinations('abcd', 2)))}")

# c) How many different permutations are there of 2 letters from "abcd"?

print(f"How many permutations of 2 letters from 'abcd': {len(list(itertools.permutations('abcd', 2)))}")

# 3) Your code should produce a list of dictionaries. Using this data, write some code that calculates 
# and outputs the following information:
profiles = json.load(open('profiles.json'))


#   - Total number of users
total_users = sum([1 for user in profiles if user['_id']])
print(f"\n# of Total Users: {total_users}")


#   - Number of active 
active_users = sum([1 for user in profiles if user['isActive']])
print(f"# of Acticve Users: {active_users}")


#   - Number of inactive users
inactive_users = sum([1 for user in profiles if not user['isActive']])
print(f"# of Inactive Users: {inactive_users}")


#   - Grand total of balances for all users
total_balance = sum([function_exercises.handle_dollar_sign_commas(user['balance']) for user in profiles])
print(f"Total balance of all users: ${total_balance}")


#   - Average balance per user
print(f"Average balance: ${round(total_balance/total_users, 2)}")


#   - User with the lowest balance
lowest_balance = function_exercises.handle_dollar_sign_commas(profiles[0]['balance'])
user_with_lowest_balance = ""
for user in profiles:
    if function_exercises.handle_dollar_sign_commas(user['balance']) < lowest_balance:
        lowest_balance = function_exercises.handle_dollar_sign_commas(user['balance'])
        user_with_lowest_balance = user['name']
print(f"User with lowest balance: {user_with_lowest_balance}")


#   - User with the highest balance
highest_balance = function_exercises.handle_dollar_sign_commas(profiles[0]['balance'])
user_with_highest_balance = ""
for user in profiles:
    if function_exercises.handle_dollar_sign_commas(user['balance']) > lowest_balance:
        lowest_balance = function_exercises.handle_dollar_sign_commas(user['balance'])
        user_with_highest_balance = user['name']
print(f"User with highest balance: {user_with_highest_balance}")


#   - Most common favorite fruit
fruit_dict = {}
for user in profiles:
    if user['favoriteFruit'] not in fruit_dict:
        fruit_dict[user['favoriteFruit']] = 1
    else:
        fruit_dict[user['favoriteFruit']] += 1
max_value = max(fruit_dict.values())

print("Favorite Fruit(s): ")
for key, value in fruit_dict.items():
    if value == max_value:
        print(key)


#   - Least most common favorite fruit
min_value = min(fruit_dict.values())

print("Least Favorite Fruit(s): ")
for key, value in fruit_dict.items():
    if value == min_value:
        print(key)


#   - Total number of unread messages for all users
list_of_numbers = []
for user in profiles:
    answer = ""
    for letter in user['greeting']:
        if letter.isdigit():
            answer += letter
    list_of_numbers.append(int(answer))

print(f"Total # of unread messages (all users): {sum(list_of_numbers)}")


