import socket
#make PEP-8 Compliant create a separate function for login 

def establish_Connection():
	#Login here
	#TODO: add a loop to ask the user to have correct credentials
	#connect to the initiated server
	s = socket.socket()
	s.connect(('127.0.0.1', 12345))
	msg = s.recv(1024).decode()
	print(msg)
	login(s)
	
	s.close()

def login(s):
	#login to the existing accounts in LOGINS check login_server.py
	print("Welcome, please Sign In.")
	username = input("Username: ")
	password = input("Password: ")
	s.sendall(username.encode())
	s.sendall(password.encode())
	server_rsp = s.recv(1024).decode()
	print(server_rsp)

def main():
	establish_Connection()

if __name__ == "__main__":
	main()		
