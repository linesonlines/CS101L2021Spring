#Lab6
#Captain Daryani
#cpd6g3@umsystem.edu

#Length of the card is 10 characters
#First 5 characters can only be A-Z
#The 6th character (at index 5) can only be 1, 2 or 3.
#The 7th character (at index 6) can only be 1, 2, 3, or 4.
#The 8th, 9th, and 10th character (index 7, 8, and 9) can only be [0-9]

import string

upper = string.ascii_uppercase
digits = string.digits

def get_school(card):
    if card[5] == "1":
        return "School of Computing and Engineering SCE"
    elif card[5] == "2":
        return "School of Law"
    elif card[5] == "3":
        return "College of Arts and Sciences"
    else:
        return "Invalid School"

def get_grade(card):
    if card[6] == "1":
        return "Freshman"
    elif card[6] == "2":
        return "Sophomore"
    elif card[6] == "3":
        return "Junior"
    elif card[6] == "4":
        return "Senior"
    else:
        return "Invalid Grade"

def character_value(letter):
    try:
        value = upper.rindex(letter.upper())
    except ValueError:
        return -1
    else:
        return value

def is_digit(letter):
    return letter in digits

def get_check_digit(card):
    check_digit = 0
    index = 0
    while index < 5:
        check_digit += (index + 1) * character_value(card[index])
        index += 1
    while index < 10:
        check_digit += (index + 1) * int(card[index])
        index += 1
    check_digit = check_digit % 10
    return int(check_digit)

def verify_check_digit(card):
    message = ""
    if len(card) != 10:
        message = "The length of the number given must be 10"
        return (False, message)
    index = 0
    while index < 5:
        if character_value(card[index]) == -1:
            message = "The first 5 characters must be A-Z, the invalid character is at " + str(index) + " is " + str(card[index])
            return (False, message)
        index += 1
    index = 7
    while index < 10:
        if is_digit(card[index]) == False:
            message = "The last 3 characters must be 0-9, the invalid character is at " + str(index) + " is " + str(card[index])
            return (False, message)
        index += 1
    if get_school(card) == "Invalid School":
        message = "The sixth character must be 1 2 or 3"
        return (False, message)
    if get_grade(card) == "Invalid Grade":
        message += "The seventh character must be 1 2 3 or 4"
        return (False, message)
    val = get_check_digit(card)
    if val != int(card[9]):
        message += "Check Digit "+card[9]+" does not match calculated value "+str(val)+"." 
        return (False, message)
    return (True, message)

#Main Program
#print(verify_check_digit("V2XYZ58BB"))
#print(verify_check_digit("V2XYZ58BBB"))
#print(verify_check_digit("VWXYZ58BBB"))
#print(verify_check_digit("VWXYZ58593"))
#print(verify_check_digit("VWXYZ38593"))
#print(verify_check_digit("VWXYZ34593"))
#print(verify_check_digit("VWXYZ34592"))

print("Linda Hall")
print("Library Card Check")
print("=======================================================================")
l_card = "start"
while (l_card != ""):
    l_card = input("\nEnter Library Card. Hit Enter to Exit ==> ")
    if (l_card != ""):
        results = verify_check_digit(l_card)
        if results[0] == False:
            print("Library card is invalid.")
            print(results[1])
        else:
            print("Library card is valid.")
            print("The card belongs to a student in",get_school(l_card))
            print("The card belongs to a",get_grade(l_card))





            
