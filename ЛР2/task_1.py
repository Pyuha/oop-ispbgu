money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
balance = money_capital - spend
month = 1


while balance > 0:
    spend += spend*increase
    balance = (balance+salary) - spend
    month += 1



print("Количество месяцев, которое можно протянуть без долгов:", month)
