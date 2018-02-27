user = str(input('Usuário: '))
passw = str(input('Senha: '))

while (user == passw):
  print('Senha não pode ser igual ao usuário!')
  passw = str(input('Senha: '))