#1. Countdown 
#create function accepts number as input and returns a list counting down by 1
def countdown(number):
    list = []
    for x in range(number, 0, -1):
        list.append(x)
    return list
new_list=countdown(19)
print(new_list)
    
#2. Print and Return 
#create function receives list with 2 numbers, print first, return second

def print_and_return(num1, num2): 
    print(num1)
    return num2
get_nums = print_and_return(12, 8)
print(get_nums)

#3. First Plus Length
#create function accepts list, 
# returns sum of first value in list added to list's length
def add_apple_and_apples(list):
    sum = list[0] + len(list)
    return sum
total = add_apple_and_apples([4,3,2,1]) 
print(total)

#4. Values Greater Than Second
#write function accepts list
#create new list containing values greater than original lists second value
#if list has 2 elements have the function return false
def values_greater_than_second(list):
    new_list=[]
    for i in range(len(list)):
        print(i)
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list
two_great = values_greater_than_second([2,6,7,10,12])
print(two_great)

#5. This Length, That Value
#write function that accepts 2 ints as parameters: size and value
#function creates and returns a list whose length = to the given size
#values are all the give value
def length_and_value(size, value):
    new_list = []
    new_list.extend([value for i in range(size)])
    return new_list
get_size_and_val = length_and_value(3,9)  
print(get_size_and_val)
