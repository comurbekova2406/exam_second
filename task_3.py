students = [
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agness', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Don', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alexey', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susanne', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Stevie', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktanbek', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]
# 1
python_ = []
java_ = []
javascript_ = []
courses = ['python', 'java', 'javascript']


def data_courses():
    for i in students:
        if i['course'] == 'python':
            python_.append(i['name'])
        elif i['course'] == 'java':
            java_.append(i['name'])
        elif i['course'] == 'javascript':
            javascript_.append(i['name'])

    names_of_courses = [python_, java_, javascript_]

    list_of_students = dict(zip(courses, names_of_courses))
    return list_of_students


print(data_courses())

# 2
names_ages = {}


def other_names(students):
    for j in students:
        names_ages.update({j['name']: j['age']})
    return names_ages


other_names(students)
print(names_ages)
# 3

names = ['Janyl', 'Nursultan', 'Meerim', 'Emir', 'Susann', 'Marcus', 'Aidin',
         'Aigerim', 'Angela', 'Albert', 'Jyldyz', 'Doe', 'Gloria', 'Aliaskar',
         'Martin', 'John', 'Andrew', 'Steve', 'Johnathan', 'Adyl', 'Chyngyz',
         'Michael', 'Atay', 'Mikkel', 'Agnes', 'Aidana', 'Sultan', 'Nash',
         'Nicolas', 'Mirbek', 'Aktan', 'Emirlan', 'Jennifer', 'Eniston', 'Alex', 'Mark']


def check_all_names(names_: object, name_ages_):
    for i in names:
        try:
            print(f'Имя {i}  : возраст {names_ages[i]}')
        except KeyError:
            print(f'Имени {i} нет в данном словаре')


check_all_names(names, names_ages)

