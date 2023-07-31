# Task 1: Update=ing Values in Dictionaries and Lists
print("Task 1: Update Values in Dictionaries and Lists")
x = [[5,2,3], [10,8,9]]
students = [{'first_name': 'Michael', 'last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'}]
sports_directory = {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'soccer': ['Messi', 'Ronaldo', 'Rooney']}
z = [{'x': 0, 'y': 20}]

# Changing values as per the task
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

# Printing the updated values
print("Updated values:")
print("x =", x)
print("students =", students)
print("sports_directory =", sports_directory)
print("z =", z)

# Task 2: Iterating Through a List of Dictionaries
print("\nTask 2: Iterate Through a List of Dictionaries")
def iterate_dictionary(some_list):
    for dictionary in some_list:
        print(', '.join([f'{key} - {value}' for key, value in dictionary.items()]))

students = [{'first_name': 'Michael', 'last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'}, {'first_name': 'Mark', 'last_name': 'Guillen'}, {'first_name': 'KB', 'last_name' : 'Tonel'}]
iterate_dictionary(students)

# Task 3: Geting Values From a List of Dictionaries
print("\nTask 3: Get Values From a List of Dictionaries")
def iterate_dictionary_2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])
    print()

iterate_dictionary_2('first_name', students)
iterate_dictionary_2('last_name', students)

# Task 4: Iterating Through a Dictionary with List Values
print("\nTask 4: Iterate Through a Dictionary with List Values")
def print_info(some_dict):
    for key, value in some_dict.items():
        print()
        print(f'{len(value)} {key.upper()}')
        for item in value:
            print(item)

dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'], 'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}
print_info(dojo)
