#Lab 12
#Captain Daryani
#cpd6g3@truman.edu

import string

def get_set(the_list):
    the_set = {"",""}
    for l in the_list:
        the_set.add(l)
    the_set.remove("")
    return the_set

def get_dict(the_set,the_list):
    the_dict = {}
    for s in the_set:
        the_dict.update({s: 0})
    for l in the_set:
        the_dict[l] = the_dict[l] + 1
    return the_dict

def get_list():
    content_list = []
    final_list = []
    stripped_list = []
    valid_input = False
    while valid_input == False:
        try:
            file_name = input("Enter the file name ==> ")
            f = open(file_name, "r")
        except FileNotFoundError:
            print("Could not open file",file_name)
        else:
            valid_input = True
    contents = f.readlines()
    f.close()
    for c in contents:
        content_list.append(c.split(" "))

    for l in content_list:
        final_list += l

    for f in final_list:
        word = (f.strip()).translate(str.maketrans('','',string.punctuation)).lower()
        if len(word) > 3:
            stripped_list.append(word)
    return stripped_list

#Main
my_list = get_list()
#print(my_list)
my_set = get_set(my_list)
#print(my_set)
my_dictionary = get_dict(my_list, my_set)
#print(my_dictionary)
list_of_numbers = list(my_dictionary.values())
list_of_numbers.sort()
#print(list_of_numbers)
top_ten = []
x = 1
while x < 10 and x < len(list_of_numbers):
    top_ten.append(list_of_numbers.pop())
    x += 1
#print(top_ten)



print("Most frequently used words")
print("==========================")
for x, y in my_dictionary.items():
    if y in top_ten:
        print(("{:<20} {:<10} ").format(x, y))





