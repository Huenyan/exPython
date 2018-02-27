from datetime import datetime
from time import sleep

print ('Hora atual: ' + (datetime.now().strftime("%H:%M:%S")))
alarm = input('Digite a hora do despetador (hh:mm): ')

while (datetime.now().strftime("%H:%M") != alarm):
  print('TIC ' + (datetime.now().strftime("%H:%M:%S")))
  sleep(1)
  print('TAC ' + (datetime.now().strftime("%H:%M:%S")))
  sleep(1)
  
print("!!DESPERTOU!!")
      