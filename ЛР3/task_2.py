def find_common_participants(a, b, c=","):
    new_a = a.split(c)
    new_b = b.split(c)
    d = list(set(new_a) & set(new_b))
    return d


first_group = "Иванов|Петров|Сидоров"
second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(first_group, second_group))
