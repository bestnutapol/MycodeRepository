import time
from pymodbus.client.sync import ModbusTcpClient
IP_Address = 'localhost'
client = ModbusTcpClient(IP_Address)
print(client.connect())
#client.write_registers(0,50)
while True:
    result = client.read_holding_registers(0,1,unit=0x01)
    print(result.registers[0])
    time.sleep(5)
client.close()