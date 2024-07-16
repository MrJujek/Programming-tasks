with open("./Dane_2305/pi_przyklad.txt") as f:
    lines = f.read()

numbers = lines.split("\n")
last_index = 0
max_array = []
current_array = []
is_growing = []
for i, number in enumerate(numbers):
    if number == '':
        continue

    current_array.append(number)

    growing = True
    if len(current_array) > 2 and current_array[-2] > current_array[-1]:
        growing = False

    is_growing.append(growing)

current_array = []
changed = False
for i, bool in enumerate(is_growing):
    if len(current_array) == 0:
        current_array.append((i, bool, numbers[i]))
        changed = False

    if current_array[-1][2] == numbers[i] and changed == False:
        print("asd", changed, current_array, (i, bool, numbers[i]))
        changed = True
    elif current_array[-1][2] == numbers[i] and changed == True:
        print("qwe", changed, current_array, (i, bool, numbers[i]))
        max_array.append(current_array)
        current_array = [(i, bool, numbers[i])]
        changed = False

    if current_array[-1][1] == bool:
        current_array.append((i, bool, numbers[i]))
    elif current_array[-1][1] != bool and changed == False:
        current_array.append((i, bool, numbers[i]))
        changed = True
    else:
        max_array.append(current_array)
        current_array = [(i,bool,numbers[i])]
        changed = False

for i in max_array:
    print(i)

max_array = max(max_array, key=len)

if int(numbers[max_array[0][0]-1]) < max_array[0][0]:
    max_array.insert(0, (max_array[0][0]-1, True, numbers[max_array[0][0]-1]))
print("\n", max_array)
answer = ""
for i in max_array:
    answer += i[2]
print(max_array[0][0]+1)
print(answer)