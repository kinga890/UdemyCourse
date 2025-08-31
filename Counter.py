my_list = [1,2,3,4,5,6,7,8,9,10]

# Solution 1

first = 0
for i in my_list:
    result = i + first
    first = result
    print(result)

print(result)

# Solution 2

result = 0

for i in my_list:
    result+= i
    print(result)


# Solution 3

prev = None

for value in my_list:
    if prev is None:
        result = value
        prev = value
    else:
        result = prev + value
        prev = result

    print(result)

# Solution 4

prev = my_list[0]
print(my_list[0])
for value in my_list[1:]:
    result = prev + value
    prev = result
    print(result)
