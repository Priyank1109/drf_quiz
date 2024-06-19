def print_pattern(n):
    for i in range(n):
        # Print the first row of stars
        if i == 0:
            print('*' * n)
        else:
            # Print the stars and spaces for the remaining rows
            print('' + ' ' * (n - i - 2) + '')

# Specify the number of rows (or height) of the pattern
n = 5
print_pattern(n)
