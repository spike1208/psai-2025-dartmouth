my_list = input("Please enter the list of numbers: ").split()
correct_number = int(input("Please enter the number you want to look for: "))
int_list = []
for i in my_list:
    int_list.append(int(i))
repeat = []
count = -1
for i in int_list:
    count = count + 1
    if correct_number == i:
        if count not in repeat:
            print(count)
            repeat.append(count)

