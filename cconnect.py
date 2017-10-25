import paramiko
import datetime
import time



class ConnectCiscoDevice():

	def __init__ (self,host,username,password):
		self.host = host
		self.username = username
		self.password = password
		
		remote_conn_pre = paramiko.SSHClient()
		remote_conn_pre
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		remote_conn_pre.connect(host, username=username, password=password, look_for_keys=False, allow_agent=False)
		print("SSH connection established to " + host)
		    
		remote_conn = remote_conn_pre.invoke_shell()
		print("Interactive SSH session established")

		output = remote_conn.recv(1000)
		print(output)   

		remote_conn.send("\n")
		remote_conn.send("show ip interface brief\n")
		time.sleep(5)

		output = remote_conn.recv(5000)
		print(output)
				

ccd=ConnectCiscoDevice('169.254.0.2','testuser','password')