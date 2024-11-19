#This is a little piece of code that will take the contents of an array and make a new array with each number doubled.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
new_numbers = []
for number in numbers:
    new_numbers += [number * 2]
print(new_numbers)
