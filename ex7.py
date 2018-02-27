sal = float(input('Digite o salário original:'))
print('\nSalário original: ' + str(sal))

if (sal <= 280):
  print('20% de reajuste.')
  print(str(sal*20/100) + ' de aumento.')
  print('Novo salário: ' + str(sal*20/100 + sal))
elif (sal > 280) and (sal <= 700 ):
  print('15% de reajuste.')
  print(str(sal*15/100) + ' de aumento.')
  print('Novo salário: ' + str(sal*15/100 + sal))
elif (sal > 700) and (sal <= 1500 ):
  print('10% de reajuste.')
  print(str(sal*10/100) + ' de aumento.')
  print('Novo salário: ' + str(sal*10/100 + sal))   
elif (sal > 1500):
  print('5% de reajuste.')
  print(str(sal*5/100) + ' de aumento.')
  print('Novo salário: ' + str(sal*5/100 + sal))   