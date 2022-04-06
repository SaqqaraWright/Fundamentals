# 1. Update Values in Dictionaries and Lists
    #(1) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    #(2) Change the last_name of the first student from 'Jordan' to 'Bryant'
    #(3) In the sports_directory, change 'Messi' to 'Andres'
    #(4) Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ] #this is a list of dictionaries that has two key valued pairs.

x[1][0]=15 #[1] points to outer array and the [0] is the inner array. They go side by side and aren't stacked within one another.
students[0]['last_name']= 'Bryant' #[0] points to the array I'm targeting and ['last_name'] points to the particular data I'm targeting within the array
# print(students[0])
sports_directory['soccer'][0]='Andres' #Note: if you can find the key you can change it ("it" referring to the data associated with it). I just used the same syntax for finding the current key at this location and then set it to equal a different data entry and voila.
print(x[0][0])
print(sports_directory['soccer'][0])
z[0]['y']=30
print(z)

#2 Iterate Through a List of Dictionaries
students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for index in range(len(students)):
    for key in students[index]:
        print(students[index][key])

iterateDictionary(students) 
should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel


#3 Get Values from a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for v in students:
    print(v)

x='first_name'
y='last_name'
    for x,y in students.items():
    print(x, y)
    iterateDictionary2(key_name, some_list)
iterateDictionary(students) 
should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

# #4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f"{len(val)} {key.upper()}") #key names are always strings and val in this case is an array #Side note: set up word wrap
        for v in val:
            print(v)
    printInfo(dojo)

# for key, val in capitals.items():
#     print(key, " = ", val)
