import paramiko
import datetime
import time
import string
import csv



class SSH_Cisco():

	def __init__ (self):

		pass


	def SendCommand(self,host,username,password,command):
		
		
		remote_conn_pre = paramiko.SSHClient()
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		remote_conn_pre.connect(host, username=username, password=password, look_for_keys=False, allow_agent=False)
		print("SSH connection established to " + host)
		    
		remote_conn = remote_conn_pre.invoke_shell()
		# print("Interactive shell established")

		remote_conn.send('terminal len 0')
		# print("Setting terminal length to 0")

		remote_conn.send("\n")
		
		output = remote_conn.recv(1000)
		# print(output)   

		remote_conn.send("\n")
		remote_conn.send(command)
		remote_conn.send("\n")
		time.sleep(5)
		# print("Command sent")

		output = str(remote_conn.recv(50000))
		# print (output)
		return (output)

		
		

conn1=SSH_Cisco()
# output = conn1.SendCommand('169.254.0.2','testuser','password','show users')


# for line in output.split("\\r\\n"):  # Note the 'double \\ to escape to a literal'
# 	print(line)

with open('routers.txt', 'r') as f_devices:
  device_username_pw = csv.reader(f_devices)
  devices = list(device_username_pw)

# print("Here is the list of the routers",devices)


outputs = ''
try:
	for ip,user,password in devices:
		outputs += conn1.SendCommand(ip,user,password,'show users')
		# outputs.append(x)
except:
	pass
	


for line in outputs.split("\\r\\n"):  # Note the 'double \\ to escape to a literal'
	print(line)


# # print (outputs)

# for line in outputs:
# 	# print (line)
# 	print ('*************************************')
# 	print(line.split("\\r\\n"))  # Note the 'double \\ to escape to a literal')



