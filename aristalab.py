#Program to fetch the output of show version and show bgp summary from the switch

from netmiko import ConnectHandler
showVersion =  "show version | json"
showBGP = "show ip bgp summary | json"

eos_device = {
    'device_type': 'arista_eos',
    'ip': '10.85.128.134',
    'username': 'auto',
    'password': 'test'
}
print('Start of program')

d = ConnectHandler(**eos_device)
showVersionOutput = d.send_command_timing(showVersion)
showBGPOutput = d.send_command_timings(showBGP)

d.disconnect()
print(showVersionOutput, showBGPOutput)
