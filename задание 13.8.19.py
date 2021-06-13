tickets = int(input("Ввыберете количество билетов"))
price = 0

for visitor in range(tickets,):
    age = int(input("Введите ваш возраст пожалйста:"))
    if age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    elif age > 25:
        price += 1390
if tickets > 3:
    price = price - (price * 0.1)
print("Сумма к оплате", price)