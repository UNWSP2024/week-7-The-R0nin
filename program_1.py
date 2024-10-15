# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
#information
print('list the rainfall by inches')
#list
rainfall = []
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']

#Inputs
while len(rainfall) < len(months):
    rainfall.append(int(input('Rainfall: ')))

#calculations
total = sum(rainfall[0:13])
average = total / 12

#Returns
print('The Total is: ', total)
print('The average is: ', average)

#min,max
print('The max is: ', max(rainfall))
print('The min is: ', min(rainfall))
