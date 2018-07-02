import socket
#make PEP-8 Compliant

#login to existing user information
def main():
	sendLoginInformation()
	
def sendLoginInformation():
	s = socket.socket()
	host = socket.gethostname()
	port = 12345
	s.connect((host, port))
	
	#Login here
	#TODO: add a loop to ask the user to have correct credentials 
	print("Welcome please Log in.")
	username = input("Username: ")
	password = input("Password: ")
	s.sendall(username.encode())
	s.sendall(password.encode())
	print(s.recv(1024).decode())
	
	#Logout here
	#TODO: loop to return back to login once logged out 
	print("Would you like to logout?")
	response = input("Yes or No >> ")
	s.sendall(response.encode())
	print(s.recv(1024).decode())
	
	s.close()
	
main()