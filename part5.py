'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below

month = input("Enter a month: ")

if month not in ['January','january', 'February','february','March', 'march', 'April', 'april', 'May', 'may', 'June', 'june' , 'July', 'july', 'August', 'august', 'September', 'september', 'October', 'october','November', 'november','December', 'december' ]:
  print("Not a month")
  
if month == 'January' or month == 'january' or month == 'March' or month == 'march' or month == 'May' or month == 'may' or month == 'July' or month == 'july' or month == 'August' or month == 'august' or month == 'October' or month == 'october' or month == 'December' or month == 'december':
  print("31 days")
if month == 'February'or month == 'february':
  print("28 days, 29 on a leap year")
if month == 'April' or month == 'april' or month == 'June' or month == 'june' or month == 'September' or month == 'september' or month == 'November' or month == 'november':
  print("30 days")
