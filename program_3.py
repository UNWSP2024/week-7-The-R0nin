# Program #3: US_Population


def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population. 
    choose = True
    while choose == True:
        print(int(input('year: ')))
        print(str(input('State name: ')))
        print(int(input('population: ')))
        another = print(int(input('Insert more data(Y/N): ')))
        if another == 'Y':
            choose = True
        if another == 'N':
            choose = False
        else:
            print('Error, no option chosen')
            choose = False
    all_entered_values = [[1,2,3][4,5,6][7,8,9]]            
main()            

    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]


    # Now have the user enter a year. 
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

#def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population


# Call the main function.
#    if __name__ == '__main__':
