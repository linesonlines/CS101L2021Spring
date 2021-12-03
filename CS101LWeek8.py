#Lab 9
#Captain Daryani
#cpd6g3@umsystem.edu
#Algorithms and explanations commented throughout code, respectively. 
import math

#prints the menu and returns the selection
def print_menu():
    print("{:10}Grade Menu".format(' '))
    print("1 - Add Test")
    print("2 - Remove Test")
    print("3 - Clear Tests")
    print("4 - Add Assignment")
    print("5 - Remove Assignment")
    print("6 - Clear Assignments")
    print("D - Display")
    print("Q - Quit\n")
    s = input("Enter your selection ==> ")
    return s

#prints the request for a number and returns the number entered
#checks to make sure the input was a number between 0.0 and 100.0
def get_num(message):
    valid_input = False
    while valid_input == False:
        try:
          num = float(input(message))
          assert 0.0 <= num <= 100.0
        except AssertionError:
          print("Invalid input. Enter a number greater than zero.")
        except ValueError:
          print("Invalid input. Enter a number greater than zero.")
        else:
          valid_input = True
          return num

#executes if the selection was display.
#calculates all needed values given the
#two lists of scores
def display(tests, asm):
    num_tests = len(tests)
    num_asm = len(asm)
    if num_tests == 0:
        max_tests = "n/a"
        min_tests = "n/a"
        mean_tests = "n/a"
        std_tests = "n/a"
    else:
        max_tests = max(tests)
        min_tests = min(tests)
        mean_tests = sum(tests) / num_tests
        std_tests = std_dev(tests)
    if num_asm == 0:
        max_asm = "n/a"
        min_asm = "n/a"
        mean_asm = "n/a"
        std_asm = "n/a"
    else:
        max_asm = max(asm)
        min_asm = min(asm)
        mean_asm = sum(asm) / num_asm
        std_asm = std_dev(asm)

    # you can't have a weighted score if the mean is "n/a"
    # so I took that into account here
    if num_tests != 0 and num_asm != 0:
        weighted = .6 * mean_tests + .4 * mean_asm
    elif num_tests == 0 and num_asm != 0:
        weighted = mean_asm
    elif num_tests != 0 and num_asm == 0:
        weighted = mean_tests
    else:
        weighted = "n/a"

    heading = ("{:20} {:10} {:10} {:10} {:10} {:10}").format("Type","#","min","max","avg","std")
    heading2 = ("=================================================================================")
    if (num_tests != 0):
        t_formatted = ("{:20} {:<10} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f}").format("Tests",num_tests,min_tests,max_tests,mean_tests,std_tests)
    else:
        t_formatted = ("{:20} {:<10} {:10} {:10} {:10} {:10}").format("Tests",num_tests,min_tests,max_tests,mean_tests,std_tests)
    if (num_asm != 0):
       a_formatted = ("{:20} {:<10} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f}").format("Programs",num_asm,min_asm,max_asm,mean_asm,std_asm)
    else:
        a_formatted = ("{:20} {:<10} {:10} {:10} {:10} {:10}").format("Programs",num_asm,min_asm,max_asm,mean_asm,std_asm)
    print(heading)
    print(heading2)
    print(t_formatted)
    print(a_formatted)
    if num_tests != 0 or num_asm != 0:
        print(("Weighted Score: {:0.2f}").format(weighted)+"\n")
    else:
        print("Weighted Score: n/a\n")

#returns the standard deviation given a list of scores
def std_dev(scores):
    num_scores = len(scores)
    mean = sum(scores) / num_scores
    deviations = []
    for x in scores:
        deviations.append((x - mean) ** 2)
    std_dev = math.sqrt(sum(deviations) / num_scores)
    return std_dev

#Main program
tests = []
assignments = []
selected_quit = False
while selected_quit == False:
    input_valid = False
    while input_valid == False:
        selection = print_menu().upper()
        if selection != "1" and selection != "2" and selection != "3" and selection != "4" and selection != "5" and selection != "6" and selection != "D" and selection != "Q":
            print("\nError: Invalid selection\n")
        else:
            input_valid = True
            if selection == "1":
              tests.append(get_num("Enter the new Test score 0-100 ==> "))
            elif selection == "2":
              try:
                  tests.remove(get_num("Enter the Test score to remove 0-100 ==> "))
              except ValueError:
                  print("Error: Could not find score to remove\n")
            elif selection == "3":
              tests.clear()
            elif selection == "4":
              assignments.append(get_num("Enter the new Assignment score 0-100 ==> "))
            elif selection == "5":
              try:
                assignments.remove(get_num("Enter the Assignment score to remove 0-100 ==> "))
              except ValueError:
                print("Error: Could not find score to remove\n")
            elif selection == "6":
              assignments.clear()
            elif selection == "D":
              display(tests, assignments)
            elif selection == "Q":
                selected_quit = True
