money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
balance = money_capital + salary

while balance > 0:
    balance -= spend
    if balance > 0:
        spend += spend*increase
        balance += salary
        month = month + 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
