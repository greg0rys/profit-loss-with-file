# *******************************************************************************
# Pseudocode:
# Author: Gregory Shenefelt
# Lab: Lab 4
# Date: 05/13/2021
# Description: A program that helps you see how much you lost on a shipment \n
#  due to markdowns
# that also validates all user input to makes sure that it is acceptable
# Input: msg – user enters (y/n) if this is their first run //
# shipmentValue – user enters any Real number
# // numItems – user enters any Integer
# // cost – user enters any real number
# // again – user enters (y/n) if they wish to work on more invoices
# Output: **Sample Run**
# “Is this your first time using the program? Enter y/n” b
# ‘Please enter y for yes -n for no’
# ‘First time? (y/n)’ N
# “Please begin entering your values”
# “Please enter the invoice total: $” 0
# “Cost cannot be less than 0”
# “Please enter the invoice total: $” 500
# “How many items would you like to markdown?” 0
# “Number of items must be more than 0”
# “How many items would you like to markdown?” 2
# “Amount off item 1: $” 0
# “Cost cannot be less than 0”
# “Amount off item 1: $” 50
# “Amount off item 2: $” 50
# “”
# “You spent: $500.00”
# “You did a total markdown for: $100.00”
# “Which is: 20.0%”
# “ Please don’t order anymore”
# “Would you like to do another invoice? Enter y/n” sure
# “Please enter y for yes – no for no” N
# “Thanks for using me!”

# Sources: course materials, gaddis book.

# //newUserMsg() asks the user if this is their first time running the program
# // if the user enters y it will let the user know how this program works
# // if the user enters n it will just tell the user to proceed

# Module newUserMsg()
# 	// Local Variable
# 	Declare String msg
# 	Display “Is this the first time using this program? Enter y/n”
#	Input msg
#	While toLower(msg) != ‘y’ and toLower(msg) != ‘n’
#		Display ‘Please enter y for yes – no for no’
#		Input msg
#	End While
# 	If msg == ‘y’ Then
# 		Display “Welcome to your first run”
#   	Display “I will ask for your invoice total, number of  markdowns,
#		Display " and the sum to reduce by”
#   	Display “I will then calculate your loss in dollars and percent”
#   	Display “And advise you if you should reorder them or not”
#   Else
# 		  Display “Please begin entering your values”
#   End If
# End Module

# // getValue() gets the total cost of the shipment and returns it

# Function Real getValue()
# 	//Declare the local variable
# 	Declare Real shipmentValue
# 	Display “Enter the total from the invoice:”
# 	Input shipmentValue
#	While shipmentValue <= 0.00
#		Display ‘Cost cannot be less than zero’
#		Display ‘Enter the total from the invoice:”
#		Input shipmentValue
#	End While
# 	Return shipmentValue
# End Function

# // the itemValue() asks the user to input the number of items that
# // need to be marked down and collects the cost of the item
# // and then returns it

# Function Real itemValue()
# 	// Declare local variables
#    Declare Integer numItems
#  	 Display “How many items would you like to markdown?”
#    Input numItems
#	 While numItems <= 0
#		Display ‘Number of items cannot be less than zero’
#		Display ‘How many items would you like to markdown?’
#		Input numItems
#    End While
# 	For counter = 1 To numItems +1
#  		 // Declare a variable to hold the cost of the item
#   		Declare Real itemVal = 0.0
#   		Declare Real cost
#   		Display “Enter the cost of item”,counter
#   		Input cost
#		    While cost <= 0.00
#			    Display ‘Cost cannot be zero’
#			    Display ‘Enter the cost of item’, counter
#			    Input cost
#		    End While
#   		Set itemVal = itemVal + cost
# 		Return itemVal
#	End For
# End Function

# // The reducedby() will take the itemCost and the shipmentValue as arguments and subtract the two then it will return the product to the markdownAmount variable
# Function Real reducedby(Declare Real x, Declare Real y)
# 	//define a local variable to hold the calculations sum
# 	Declare Real sum
# 	Set sum = x – y
# 	Return sum
# End Function

# // the lossPercent() will take the shipmentValue and itemCost as arguments and convert it to a percent
# Function Real lossPercent(declare Real a, Real b)
# 	//Declare the local variable
# 	Declare Real perHundred
# 	perHundred = (b/a) * 100
#	Set perHundred = floatFormat(perHundred, ‘.1f’)
# 	Return perHundred
# End Function

# // the lossAlert(real z) module will take the itemCost as an argument and depending on the amount will output a message

# Function String lossAlert(declare Real z)
# 	// Determine the message to output to the user
#	// Declare the variable to hold the message
#	Declare String advisement
# 	If z > 100 Then
# 		Set advisement = “High losses reported, please review order flow”
# 	Else If z > 35 Then
# 		Set advisement = “Please don’t order anymore”
# 	Else
# 		Set advisement = 'Low losses reported'
# 	End If
# 	Return advisement
# End Function

# // Loss report is the final step of the program
# // It will output the calculation preformed to the user
# // It takes shipmentValue,itemCost,markdownPercetange, and message
# // as arguments

# Module lossReport(declare real sv , ic , mp , declare string advice)
# 	Display “You spent: $”,  sv
# 	Display “You did a total markdown for: $”, ic
# 	Display “Which is”, mp,”%”
#	Display advice
# End Module
# // the doAnother function will ask the user if they would like to work on more
#
# Module doAnother()
#	// Declare a flag for the while loop
#	Declare Boolean again
#	Set again = False
#	// use a while loop to loop back through the program if the user wants
#	While again == False
#		Display ‘Would you like to do another invoice? Enter (y/n)’
#		Input again
#		While toLower(again) != ‘y’ and toLower(again) !=’n’
#			Display ‘Please enter y for yes – n for no’
#			Input again
#		End While
#		If again == ‘y’ Then
#			Call main()
#		Else
#			Display ‘Thanks for using me!’
#		End If
#	End While
# End Module
# // The main module will only make calls to the functions
# Module main ()
# 	// Local Variables
# 	Declare String firstRun, message
# 	Declare Real shipmentValue, itemCost , markdownAmount
# 	Declare Real markdownPercentage
#	Declare Real report
#	Declare String again
# 	Set firstRun = newUserMsg()
# 	Set shipmentValue = getValue()
#	Set itemCost = itemValue()
# 	Set markdownAmount = redeucedby(shipmentValue,itemCost)
# 	Set markdownPercentage = lossPercent(shipmentValue,itemCost)
#	Set message = lossAlert(itemCost)
#	Set report = lossReport(shipmentValue, itemCost, markdownPercentage,message)
#	Set again = doAnother
# End Module
# Call main()
# *******************************************************************************
# Begin Python Program
import datetime

def login():
    y = datetime.datetime.now()
    y = y.strftime('%I' +  ':'+'%M'+'%p ' + '' + '%m'+'-'+'%Y')
    # play with inputs from the user
    managers = ['GREGS', 'GUEST', ]
    print('For test purposes please login with username guest')
    # validate the users input
    while  True:
        try:
            userLogin = input('Please enter your username to continue: ')
            if not userLogin.isalpha():
                raise Exception
        except :
            print('Error: Username must only be letters')
            continue
        else:
            break

    # for test purposes you can use admin as the username this is not case sensative
    userLogin = userLogin.upper()
    if userLogin not in managers:
        print(userLogin + ' is not an authorized manager ')
        isManager = False
    else:
        print('Welcome back' + ' ' + userLogin)
        # output the current date and time for the user for quick ref. if the user needs to fill it out on a form etc
        print('It is currently:' + y)
        isManager = True
    return isManager, userLogin


def newUserMsg():
    msg = input('Is this your first time using this program? Enter y/n ')
    msg = msg.lower()
    while msg != 'y' and msg != 'n':
        print('Please enter y for yes - n for no')
        msg = input('First time? (y/n)')
        msg = msg.lower()
    print(" ")
    if msg == 'y':
        print('Welcome to your first run')
        print('I will ask you for your invoice total, number of markdowns, and the value to reduce by')
        print('I will then calculate your loss in dollars and percent')
        print('and advise you if you should reorder them or not')
        print('   ')
    else:
        print('Please login to continue')
        print(' ')
# define the getValue() module
# Which will get the total of the invoice from the user


def getValue():
    while True:
        try:
            purchaseValue = float(input('Please enter the invoice total: $'))
            if purchaseValue <= 0.00:
                raise ValueError
        except ValueError:
            print('Cost cannot be less than zero')
            continue
        else:
            break
    return purchaseValue

# define the itemValue module
# Using a user controlled for loop and an accumulator we will collect the cost of each item
# and return their total


def itemValue():
    # Run a for loop controled by the input of numItems
    itemVal = 0.00
    while True:
        try:
            numItems = int(input('How many items would you like to '
                                 'markdown?: '))
            if numItems <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print('Number of items must be more than 0')
            continue

    # Run a for loop controled by the input of numItems
      # Run a for loop controled by the input of numItems
    for counter in range(1, numItems + 1):
        # use a nested while True loop to validate that the cost
        # is not 0; if it is keep telling the user
        while True:
            try:
                cost = float(input('amount off item ' + str(counter) + ' $'))
                if cost <= 0.00:
                    raise ValueError
            except ValueError:
                print('Cost cannot be less than zero')
                continue
            # if the cost is all good - break out of this loop
            # and continue with the for loop
            else:
                break
        itemVal = itemVal + cost
    return itemVal

# Declare the redeuced by module to calculate the sum of the markdowns


def redeucedby(x, y):
    sum = x - y
    return sum

# declare the lossPercent() which will take the shipmentValue and
# markdownAmount as arguments to conver the loss to a percentage


def lossPercent(a, b):
    # corrected the calculation
    perHundred = (b/a) * 100
    perHundred = format(perHundred, '.1f')
    return perHundred

# declare the lossAlert()
# Which uses a decision structure to decide which message to output
# which takes markdownPercentage as an argument


def lossAlert(z):
    advise = ''
    print(' ')
    if z > 100:
        advise = 'High losses reported, please review order flow '
    elif z > 30:
        advise = ' Please don\'t order anymore'
    else:
        advise = 'Low losses reported.'
    return advise


def lossReport(sv, ic, mp, advice):
    print(' ')
    print('You spent: $', format(sv, ',.2f'), sep='')
    print('You did a total markdown for: $', format(ic, ',.2f'), sep='')
    print('Which is: ', mp, '%', sep='')
    print(advice)
    print('')


#  this function manipulates the list to format it for file output
def accessList(itemCost, userName):
    x = datetime.datetime.now()
    x = x.strftime('%I' +  ':'+'%M'+'%p ' + '' + '%m'+'-'+'%Y')
    itemCostFormatted= format(itemCost, ',.2f') 
    totalLoss = []
    totalLoss.insert(0, 'User:')
    totalLoss.insert(1, userName)
    totalLoss.insert(2, 'Amount Off:(in dollars)')
    totalLoss.insert(3,itemCostFormatted)
    totalLoss.insert(4, 'Date & Time:')
    totalLoss.insert(5, x)
    return totalLoss

# This function takes the list in as an argument and writes it to a file
# using a for loop to step through the list

def lossFile(extractedData):
    fileData = list(extractedData)
    size = len(fileData)
    output = open('lossreport.txt', 'a')
    for i in range(size):
        output.write(fileData[i]+ ' ' + '\n')
    output.close()
    while True:
        try:
            viewReport = input('Would you like to view the data stored in the report? Enter (y/n): \n')
            viewReport = viewReport.lower()
            if viewReport != 'y' and viewReport != 'n':
                raise Exception
        except:
            print('Please enter y for yes - n for no')
            continue
        else:
            break
            

    if viewReport == 'yes' or viewReport == 'y':
        outprint = True
        return outprint
    else:
        outprint = False
        return outprint

# The read file module will allow the user to view the data that has been
# stored in the file using a loop to step through the file list


def readfile(readFile):
    if readFile:
        file = open('lossreport.txt', 'r')
        readList = file.readlines()
        file.close()
        for i in readList:
            print(i)
    else:
        print('Data successfully exported to lossreport.txt')


# again lets the user do another invoice if they would like
def doAnother(u):
    again = False
    while again == False:
        again = input('Would you like to do another invoice? Enter (y/n)')
        again = again.lower()
        while again != 'y' and again != 'n':
            again = input('Please enter y for yes - n for no: ')
            again = again.lower()
        if again == 'y' or again == 'yes':
            shipmentValue = getValue()
            itemCost = itemValue()
            markdownAmount = redeucedby(shipmentValue, itemCost)
            markdownPercentage = lossPercent(shipmentValue, itemCost)
            message = lossAlert(itemCost)
            report = lossReport(shipmentValue, itemCost,
                                markdownPercentage, message)
            extractList = accessList(itemCost, u)
            outF = lossFile(extractList)
            reportOut = readfile(outF)
            again = doAnother(u)

        else:
            print('Thanks for using me!')
            break

# declare the main()


def main():
    firstRun = newUserMsg()
    access, workingUser = login()
    if access:
        shipmentValue = getValue()
        itemCost = itemValue()
        markdownAmount = redeucedby(shipmentValue, itemCost)
        markdownPercentage = lossPercent(shipmentValue, itemCost)
        extractList = accessList(itemCost, workingUser)
        outF = lossFile(extractList)
        message = lossAlert(itemCost)
        report = lossReport(shipmentValue, itemCost,
                            markdownPercentage, message)
        reportOut = readfile(outF)
        again = doAnother(workingUser)


main()
