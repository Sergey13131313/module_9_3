first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result   = (x[0] - x[1] for x in zip([len(x) for x in first], [len(x) for x in second]) if x[0] != x[1])
print(list(first_result))


second_result = (len(first[i]) - len(second[i]) for i in range(len(first)))
print(list(second_result))