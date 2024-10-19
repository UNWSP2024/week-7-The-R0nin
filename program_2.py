# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.
number = 5
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def main():

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')

print(f'List of numbers that are larger than {number}:')
a = 0
while a < len(number_list):
    print(number < number_list[a])
    if number < number_list[a]:
        print(number_list[a])
    a = a + 1
# Call the main function.

if __name__ == '__main__':
    main()
