# Program #3: US_Population

def main():
    year_list = []
    s_name = []
    population = []    
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population. 
    rounds = 0 
    while rounds < 3 :
        year = int(input('year: '))
        state = str(input('State name: '))
        pop = int(input('population: '))
        year_list.append(year)
        s_name.append(state)
        population.append(pop)
        print(year_list[rounds], s_name[rounds], population[rounds])
        rounds = rounds + 1

    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]

    all_entered_values = print("Final list: ", year_list, s_name, population)
    
    # Now have the user enter a year. 
    selected_year = int(input('Select year: '))
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    year_to_sum = sum(population)

    return year_to_sum, all_entered_values

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    year_to_sum = sum(all_entered_values)
    # print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()    
