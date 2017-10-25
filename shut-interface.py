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
		remote_conn.send('terminal len 0')
		remote_conn.send("\n")
		output = remote_conn.recv(1000)
		remote_conn.send("\n")
		remote_conn.send(command)
		remote_conn.send("\n")
		time.sleep(5)
		output = str(remote_conn.recv(50000))
		return (output)


ip = '169.254.0.2'
user= 'testuser'
password = 'password'
outputs = ''

conn1 = SSH_Cisco()

outputs += conn1.SendCommand(ip,user,password,'show ip int brief')

with open('interfaces.txt', 'r') as f_interfaces:
  interfaces_to_shut= csv.reader(f_interfaces)
  shut_these_down = list(interfaces_to_shut)

print("Here is the list of the interfaces to be shut down", shut_these_down)

try:
	for interface in shut_these_down:
		if interface:
			command = 'config t' + '\n' + 'interface ' + str(interface)[2:-2] + '\n' + 'no shut' + '\n' + 'exit' + '\n'
			print(command)
			outputs += conn1.SendCommand(ip,user,password,command)
except:
	print ('exception')
	pass
	
conn1=SSH_Cisco()
outputs += conn1.SendCommand(ip,user,password,'show ip int brief')

for line in outputs.split("\\r\\n"):  # Note the 'double \\ to escape to a literal'
	print(line)
	
		
# for ip in ips:
#     try:
#         dssh.connect(ip, username='cisco', password='cisco', timeout=4)
#         stdin, stdout, stderr = ssh.exec_command('sh ip ssh')
#         print ip + '===' + stdout.read()
#         ssh.close()
#     except paramiko.AuthenticationException:
#         print ip + '=== Bad credentials'
#     except paramiko.SSHException:
#         print ip + '=== Issues with ssh service'
#     except socket.error:
#         print ip + '=== Device unreachable' 