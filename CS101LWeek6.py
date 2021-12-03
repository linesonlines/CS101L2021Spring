#Lab 7
#Captain Daryani
#cpd6g3@umsystem.edu
#All algorithms and explanations are commented throughout the program, respetively.
import string

#constants from the string module
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punct = string.punctuation

#finds the character to replace if encoding.
#it looks in each of the four constants,
#finds the index in the correct constant string,
#adds to that index (using the parameter 'num'),
#and then returns the replacement
def e_find_replacement(char, num):
    if char in lower:
        index = lower.rindex(char)
        replacement = lower[index+num]
    elif char in upper:
        index = upper.rindex(char)
        replacement = upper[index+num]
    elif char in digits:
        index = digits.rindex(char)
        replacement = digits[index+num]
    elif char in punct:
        index = punct.rindex(char)
        replacement = punct[index+num]
    else:
        return char
    return replacement

#finds the character to replace id decoding.
#it looks in each of the four constants,
#finds the index in the correct constant string,
#subtracts from that index (using the parameter 'num'),
#and then returns the replacement
def d_find_replacement(char, num):
    if char in lower:
        index = lower.rindex(char)
        replacement = lower[index-num]
    elif char in upper:
        index = upper.rindex(char)
        replacement = upper[index-num]
    elif char in digits:
        index = digits.rindex(char)
        replacement = digits[index-num]
    elif char in punct:
        index = punct.rindex(char)
        replacement = punct[index-num]
    else:
        return char
    return replacement

#prints the menu and returns the selection
def print_menu():
    print("MAIN MENU:")
    print("1) Encode a string")
    print("2) Decode a string")
    print("Q) Quit")
    s = input("Enter your selection ==> ")
    return s

#prints the request for a number and returns the number entered
#checks to make sure the input was a number greater than zero
def get_num():
    valid_input = False
    while valid_input == False:
        try:
          num = int(input("Enter the number to shift letters by: "))
          assert 1 <= num
        except AssertionError:
          print("Invalid input. Enter a number greater than zero.")
        except ValueError:
          print("Invalid input. Enter a number greater than zero.")
        else:
          valid_input = True
          return num

#calls get_num() and calls the replacement function.
#it then appends to an empty string with each replacement character
#until the new string is the same length as the old string
def encode(orig_string):
    n = get_num()
    final_string = ""
    i = 0
    while len(final_string) != len(orig_string):
        final_string += e_find_replacement(orig_string[i], n)
        i += 1
    return final_string

#calls get_num() and calls the replacement function.
#it appends to an empty string with each replacement character
#until the new string is the same length as the old string
def decode(orig_string):
    n = get_num()
    final_string = ""
    i = 0
    while len(final_string) != len(orig_string):
        final_string += d_find_replacement(orig_string[i], n)
        i += 1
    return final_string

#Main program
selected_quit = False
while selected_quit == False:
    input_valid = False
    while input_valid == False:
        selection = print_menu().upper()
        if selection != "1" and selection != "2" and selection != "Q":
            print("\nError: Invalid selection\n")
        else:
            input_valid = True
            #calls encode if the input was 1
            if selection == "1":
                user_txt = input("Enter a brief text to encrypt: ")
                print("\nEncrypted:",encode(user_txt),"\n")
            #calls decode if the input was 2
            elif selection == "2":
                user_txt = input("Enter a brief text to decrypt: ")
                print("\nDecrypted:",decode(user_txt),"\n")
            #ends the program if the input was q
            elif selection == "Q":
                selected_quit = True
