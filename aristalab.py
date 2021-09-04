#Program to upgrade the switch to a specific version

from netmiko import ConnectHandler
showVersion =  "show version | json"

eos_device = {
    'device_type': 'arista_eos',
    'ip': '10.85.128.134',
    'username': 'auto',
    'password': 'test'
}
print('Start of program')

d = ConnectHandler(**eos_device)
output = d.send_command(showVersion)

d.disconnect()
print(output)
