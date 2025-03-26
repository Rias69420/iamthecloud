numbers = [1, 10, 159, 64, 7, 3, 9]
max_value = numbers[0]

for number in numbers[1:]:
    if number > max_value: 
     max_value = number

print(max_value)