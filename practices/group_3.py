my_list = input("Please enter the list of numbers: ").split()
correct_number = int(input("Please enter the number you want to look for: "))
int_list = []
for i in my_list:
    int_list.append(int(i))
for i in int_list:
    if correct_number == i:
        print(int_list.index(i))