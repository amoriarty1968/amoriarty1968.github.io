import csv
import re
import os

#   Search a file for a cisco part number


devices =[]
device_type = []
os.chdir('C:')
files = (os.listdir())

f_output=''

for file in files:
	with open(file, 'r') as f_device:
		for line in f_device.readlines():
			if 'PID' in line:
				# Match - PID: WS-C3750V2-48PS-S , VID: V05, SN: FDO1441X2GC
				switch=re.search('WS[-][\w]+[-][\w]+[-][\w]+',line)
				if switch:
					sn=re.search('[\w]{3}[\d]{4}[\w]{3}',line)
					# print(switch.group(0),sn.group(0))
					devices.append(str([switch.group(0),sn.group(0)]))
					device_type.append(str([switch.group(0)]))

	f_device.close()

s_devices = set(device_type)

for each in s_devices:
	print('You have ' + str(device_type.count(each)) + ' Model ' + each)

print('\n')
print('You have a total of '+ str(len(devices)) + ' swtiches')


