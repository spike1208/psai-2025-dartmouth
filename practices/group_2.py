with open('will.txt', 'r', encoding='utf-8-sig') as f:
    my_list = f.readlines()
int_list = []
for i in my_list:
        int_list.append(int(i))

for i in range (len(int_list)):
    for i in range (len(int_list)-1):
        num1 = int_list[i]
        num2 = int_list[i+1]
        if num1 > num2:
            int_list[i]=num2
            int_list[i+1]=num1
print(int_list)


