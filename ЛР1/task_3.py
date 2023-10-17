list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count = len(list_players)//2

first_team = list_players[count:]
second_team = list_players[:count]

print(first_team)
print(second_team)
