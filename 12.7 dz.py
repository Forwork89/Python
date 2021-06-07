text = int(input('money'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
deposit.append(text * per_cent['ТКБ']/100)
deposit.append(text * per_cent['СКБ']/100)
deposit.append(text * per_cent['ВТБ']/100)
deposit.append(text * per_cent['СБЕР']/100)

print (deposit)

#u = list(set(text))
#print("Количество1 уникальных символов: ", len(u))