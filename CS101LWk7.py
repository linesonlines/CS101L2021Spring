#Lab 8
#Captain Daryani
#cpd6g3@umsystem.edu
#Algorithms and Explanations commented throughout code, respectively.
import csv

#prints the request for a number and returns the number entered
#checks to make sure the input was a number between 0.0 and 100.0
def get_num():
    valid_input = False
    while valid_input == False:
        try:
          num = float(input("Enter the minimum mpg ==> "))
          assert 0.0 <= num <= 100.0
        except AssertionError:
          print("Fuel economy must be number between 0 and 100.")
        except ValueError:
          print("You must enter a number for the fuel economy")
        else:
          valid_input = True
          return num


#prints the request for the input file
#checks to make sure the input file is valid
#throws FileNotFoundError if needed
#returns the file
def get_input():
    valid_input = False
    while valid_input == False:
        try:
          file_name = input("Enter the name of the input vehicle file ==> ")
          with open(file_name, 'r') as file:
              csvreader = csv.reader(file, delimiter='\t')
              header = next(csvreader)
              rows = []
              for row in csvreader:
                rows.append(row)
        except FileNotFoundError:
          print("Could not open file",file_name)
        else:
          valid_input = True
          file.close()
          return rows
          
#prints the request for the output file
#checks to make sure the output file is valid
#throws IOError if needed
#returns the file
def get_output(rows, cmpg):
    valid_input = False
    while valid_input == False:
        try:
          file_name = input("Enter the name of the file to ouput to ==> ")
          f = open(file_name, "w")
        except IOError:
          print("There is an IO Error",file_name)
        else:
          valid_input = True

    for row in rows:
      try:
        float(row[7])
      except ValueError:
        print("Could not convert value",str(row[7]),"for vehichle",str(row[0]),str(row[1]),str(row[2]))
      else:
        if float(row[7]) >= cmpg:
          ymm = row[0] + " " + row[1] + " " + row[2]
          formatted = ("{:<40}").format(ymm)
          c_form = ("{:>10.2f}").format(float(row[7]))
          f.write(formatted + c_form)
          f.write("\n")
    
#Main program
mpg = get_num()
rows_of_cars = get_input()
my_output = get_output(rows_of_cars, mpg)


