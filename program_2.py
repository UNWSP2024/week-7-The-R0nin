# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.

def main():
    # Declare local variables
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')
    
    # Display the list of numbers that are larger
    # than the number.
    print(f'List of numbers that are larger than {number}:')
    print(number < number_list[0])
    if number_list[0] == False:
        number_list.remove(number_list[0])

    print(number < number_list[1])
    if number_list[1] == False:
        number_list.remove(number_list[1])

    print(number < number_list[2])
    if number_list[2] == False:
        number_list.remove(number_list[2])

    print(number < number_list[3])
    if number_list[3] == False:
        number_list.remove(number_list[3])

    print(number < number_list[4])
    if number_list[4] == False:
        number_list.remove(number_list[4])

    print(number < number_list[5])
    if number_list[5] == False:
        number_list.remove(number_list[5])

    print(number < number_list[6])
    if number_list[6] == False:
        number_list.remove(number_list[6])

    print(number < number_list[7])
    if number_list[7] == False:
        number_list.remove(number_list[7])

    print(number < number_list[8])
    if number_list[8] == False:
        number_list.remove(number_list[8])

    print(number < number_list[9])
    if number_list[9] == False:
        number_list.remove(number_list[9])

    print(f'{number_list}')
    # Call the display_larger_than_n_list function,
    # passing a number and number list as arguments.

    display_larger_than_n_list(number, number_list)
    n = int(input('Number: '))
    n_list = number_list   
    print(n < n_list[0])
    print(n < n_list[1])
    print(n < n_list[2])
    print(n < n_list[3])
    print(n < n_list[4])
    print(n < n_list[5])
    print(n < n_list[6])
    print(n < n_list[7])
    print(n < n_list[8])
    print(n < n_list[9])
    print(f'{n_list}')

# The display_larger_than_n_list function accepts two arguments:
# a list, and a number. The function displays all of the numbers
# in the list that are greater than the number.
def display_larger_than_n_list(n, n_list):
    # Write your code to display all of the numbers in the list that are greater than then number n. below
    print('In display_larger_than_n_list')


# Call the main function.

if __name__ == '__main__':
    main()

