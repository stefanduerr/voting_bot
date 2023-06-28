import random

# Dictionary to remember the last index at which each number appeared.
# Keys are the numbers, values are the indices.
last_index = {}

# The list to store the generated numbers.
numbers = []

# Generate 100 numbers (change this if you want more or fewer numbers).
for i in range(84):

    # This loop continues generating random numbers until it finds a suitable one.
    while True:

        # Generate a random integer from 0 to 99.
        num = random.randint(0, 99)

        # If the number hasn't been used yet (isn't a key in the dictionary) or the
        # difference between the current index and the last index at which this number
        # was used is 10 or more, then we've found a suitable number and we can exit the loop.
        if num not in last_index or i - last_index[num] >= 20:
            break

    # Update the last index at which this number was used.
    last_index[num] = i

    # Add the number to the list.
    numbers.append(num)

# Print the list of generated numbers.
print(numbers)