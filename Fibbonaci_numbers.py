
# 0 1 1 2 3 5 8 13 21

# generator

def fibgenerator(num):

    first = 0
    second = 1
    print(first)
    print(second)

    for i in range(num):
        third = first + second
        first = second
        second = third
        yield third

for i in fibgenerator(20):
    print(i)


# list

my_list=[0,1,2,3,4,5,6,7,8,9,10]

first = 0
second = 1
print(first)
print(second)

for i in my_list:
    third = first + second
    first = second
    second = third
    print(third)



