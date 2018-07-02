import socket
#make PEP-8 Compliant create a separate function for login 

def main():
	sendLoginInformation()
	
def sendLoginInformation():
	"""login to existing user information"""
	s = socket.socket()
	s.connect(('127.0.0.1', 12345))
	
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