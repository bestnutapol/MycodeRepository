import time
from pymodbus.client.sync import ModbusTcpClient
import datetime
IP_Address = 'localhost'
client = ModbusTcpClient(IP_Address)
print(client.connect())
#client.write_coil(0,True)
#client.write_registers(0,50)
address_count = 10
old = []
for i in range(address_count): old.append('')
while True:
    x = datetime.datetime.now()
    result = client.read_holding_registers(0,address_count,unit=0x01)

    h = result.registers
    for j in range(address_count):
        if old[j] != h[j]:
            if old[j] != '':
                print( 'Time : '+ str(x) +' Address : '+ str(j) +' Value : '+ str(h[j]))
            old[j] = h[j]

    time.sleep(0.1)
client.close()