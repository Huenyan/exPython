p1 = float(input('Produto 1: '))
p2 = float(input('Produto 2: '))
p3 = float(input('Produto 3: '))

if (p1 == p2) and (p2 == p3):
  print('Todos possuem o mesmo preço.\n')
elif (p1 == p2) and (p1 < p3):
  print('P1 e P2 são os mais baratos.\n')
elif (p1 == p3) and (p1 < p2):
  print('P1 e P3 são os mais baratos.\n')
elif (p2 == p3) and (p2 < p1):
  print('P2 e P3 são os mais baratos.\n')
elif (p1 < p2) and (p1 < p3):
  print('P1 é o mais barato.\n')
elif (p2 < p3) and (p2 < p1):
  print('P2 é o mais barato.\n')
elif (p3 < p1) and (p3 < p2):
  print('P3 é o mais barato.\n')
