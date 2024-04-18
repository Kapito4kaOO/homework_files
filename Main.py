dict = {}

with open('1.txt', 'r', encoding = 'utf-8') as f:
    lines_1 = f.readlines()
    dict[len(lines_1)] = [lines_1, '1.txt']

with open('2.txt', 'r', encoding='utf-8') as f:
    lines_2 = f.readlines()
    dict[len(lines_2)] = [lines_2, '2.txt']

sorted_dict = sorted(dict.items())

with open('3.txt', 'w', encoding = 'utf-8') as f1:
    for i in sorted_dict:
        print(i[1][1], file=f1)
        print(i[0], file=f1)
        for j in i[1][0]:
            print(j.strip(), file=f1)

