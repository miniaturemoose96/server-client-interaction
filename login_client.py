import socket
#make PEP-8 Compliant create a separate function for login 

def establish_Connection():
	#Login here
	#TODO: add a loop to ask the user to have correct credentials
	#connect to the initiated server
	while True:
		s = socket.socket()
		s.connect(('127.0.0.1', 12345))
		msg = s.recv(1024).decode()
		print(msg)
		login(s)
	
def login(s):
	#the user is not logged in yet 
	logged_in = False
	
	if logged_in:
		#assuming client is still not logged in 
		s.close()
	elif not logged_in:
		#login to the existing accounts on server.py
		print("Welcome, please Login")
		username = input("Username: ")
		password = input("Password: ")
		s.sendall(username.encode())
		s.sendall(password.encode())	
		server_rsp = s.recv(1024).decode()
		print(server_rsp)
		s.close()

def main():
	establish_Connection()

if __name__ == "__main__":
	main()		
