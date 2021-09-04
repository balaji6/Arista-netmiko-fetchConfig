#Program to fetch the output of show version from the switch

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
output = d.send_command_timing(showVersion)

d.disconnect()
print(output)
