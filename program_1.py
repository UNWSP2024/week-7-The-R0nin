# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
print('list the rainfall by inches')
#list
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
#Inputs
months[0] = int(input('Rainfall for Jan: '))
months[1] = int(input('Rainfall for Fab: '))
months[2] = int(input('Rainfall for Mar: '))
months[3] = int(input('Rainfall for Apr: '))
months[4] = int(input('Rainfall for May: '))
months[5] = int(input('Rainfall for Jun: '))
months[6] = int(input('Rainfall for Jul: '))
months[7] = int(input('Rainfall for Aug: '))
months[8] = int(input('Rainfall for Sept: '))
months[9] = int(input('Rainfall for Oct: '))
months[10] = int(input('Rainfall for Nov: '))
months[11] = int(input('Rainfall for Dec: '))
#calculations
total = sum(months[0:13])
average = total / 12
#Returns
print('The Total is: ', total)
print('The average is: ', average)
print('The max is: ', max(months))
print('The min is: ', min(months))
