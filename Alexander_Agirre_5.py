revenue = int(input("какая была выручка?: "))
costs = int(input("Какие были издержки?: "))
staff = int(input("Сколько  у вас сотрудникков?"))
if costs < revenue:
    print("Ваша компания работает в прибыль")
    profit = revenue - costs
    profitability = (profit / revenue) * 100
    print(f"Рентабильность выручки = {int(profitability)}%")
    profit_staff = profit / staff
    print(f"Прибыль каждого сотрудника ={int(profit_staff)}")
else:
    print("Ваша компания работает в убыток")
