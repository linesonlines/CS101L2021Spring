#CS 101 Lab
#Program 4
#Name Captain Daryani
#Email cpd6g3@umsystem.edu
#PROBLEM : Making sure the program builds upon itself through process of elimination.
#ALGORITHM : mod3 + mod5 + mod7 = the accurate number - full algorithm below.
#ERROR HANDLING: Chnaged each value if above 100 or below zero.
#OTHER COMMENTS: 

print('Welcome to the Flarsheim Guesser!')
play_again = True
while play_again == True:
    print('Please think of a number between and including 1 and 100.')

    valid3 = False

    while valid3 == False:
        div3 = int(input('What is the remainder of your number when divided by 3 => '))
        if div3 != 0 and div3 != 1 and div3 != 2:
            print('your number must be a value greater than or equal to 0 and less than 3')
        else:
            valid3 = True

    valid5 = False

    while valid5 == False:
        div5 = int(input('What is the remainder of your number when divided by 5 => '))
        if div5 != 0 and div5 != 1 and div5 != 2 and div5 != 3 and div5 !=4:
            print('your number must be a value greater than or equal to 0 and less than 5')
        else:
            valid5 = True

    valid7 = False

    while valid7 == False:
        div7 = int(input('What is the remainder of your number when divided by 7 => '))
        if div7 != 0 and div7 != 1 and div7 != 2 and div7 != 3 and div7 != 4 and div7 != 5 and div7 !=6:
            print('your number must be a value greater than or equal to 0 and less than 7')
        else:
            valid7 = True

    possible_answer = 1
    while possible_answer < 101:
        test3 = possible_answer % 3
        test5 = possible_answer % 5
        test7 = possible_answer % 7
        if test3 == div3 and test5 == div5 and test7 == div7:
            the_right_answer = possible_answer
            print("The right answer is",the_right_answer)
            break
        
        possible_answer += 1
    valid_again = False
    while valid_again == False:
        again = str(input('Would you like to play again? (y or n)'))
        if again == 'y':
            play_again = True
            valid_again = True
        elif again == 'n':
            play_again = False
            valid_again = True
        else:
            print('Only inputs y and n are valid')
        



               
