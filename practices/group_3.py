my_list = input("Please enter the list of numbers: ").split()
correct_number = int(input("Please enter the number you want to look for: "))
int_list = []
for i in my_list:
    int_list.append(int(i))
repeat = []
count = 0
for i in int_list:
    if correct_number == i:
        if count not in repeat:
            print(count)
            repeat.append(count)
    if repeat == [] and count == len(int_list)-1:
        print("your number is not in list")
    count = count + 1


