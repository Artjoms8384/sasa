print('No 2 precess, bus atlaide')
dz = int (input('Izveles produktu daudzums'))
summ = dz *2.35
print(summ)

if dz >=2:
  print('Jusu atlaide ir 10%')
  atl = summ *10/100
  at = round(summ - atl,2)
  print('Cena par pirkumiem ir ' + str(at))
  else:
    print ('Jums nav atlaide')