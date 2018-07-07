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
	
def login(s):
	#This is the users first time, ask for credentials
	logged_in = False
	while not logged_in:
		#login to the existing accounts on server
		print("Welcome, please Login")
		username = input("Username: ")
		password = input("Password: ")
		s.sendall(username.encode())
		s.sendall(password.encode())
		server_rsp = s.recv(1024).decode()
		if "Welcome" in server_rsp:
			logged_in = True
			print(server_rsp)
			break
		else:
			logged_in = False
			print(server_rsp)
			continue
	else:
		print(f"You are logged in as {username}")
		s.close()

def main():
	establish_Connection()

if __name__ == "__main__":
	main()		
