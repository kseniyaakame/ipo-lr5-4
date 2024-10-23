s = input('введите строку ')
d = s.split()
result = []
for i in d:
    result.append(i[-1] + i[1:-1] + i[0])
print(result)