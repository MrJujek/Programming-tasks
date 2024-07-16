with open("./Dane_2305/pi_przyklad.txt") as f:
    lines = f.read()

numbers = lines.split("\n")
current_array = []
array = []
growing = True

for i, number in enumerate(numbers):
    if number == '':
        continue

    if len(current_array) == 0:
        current_array.append((i, number))
        continue

    if int(current_array[-1][1]) < int(number) and growing == True:
        current_array.append((i, number))
    elif int(current_array[-1][1]) > int(number) and growing == False:
        current_array.append((i, number))
    else:
        if growing == True:
            growing = False
            current_array.append((i, number))
        else:
            array.append(current_array)
            current_array = [(i, number)]
            growing = True

max_list = max(array, key=len)

if int(max_list[0][1]) > int(numbers[int(max_list[0][0]) - 1]):
    max_list.insert(0, (int(max_list[0][0]) - 1, numbers[int(max_list[0][0]) - 1]))

print(max_list[0][0] + 1)  # dodajemy jeden bo indeksy w listach są od zera
answer = ""
for i in max_list:
    answer += i[1]
print(answer)
