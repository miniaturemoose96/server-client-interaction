import socket
import sys
"""
    TODO: Create a menu function that asks the user to do something
"""


def establish_connection():   
	# connect to the initiated server
	s = socket.socket()
	s.connect(('127.0.0.1', 12345))
	msg = s.recv(1024).decode()
	print(msg)
	return s

	
def login(s):
	# This is the users first time, ask for credentials
	logged_in = False
	while not logged_in:
		# login to the existing accounts on server
		print("Welcome, please Login")
		username = input("Username: ")
		password = input("Password: ")
		s.sendall(username.encode())
		s.sendall(password.encode())
		server_rsp = s.recv(1024).decode()
		if "Success" in server_rsp:
			logged_in = True
			print(f"Welcome, {username}")
		else:
			logged_in = False
			print("Incorrect Username/Password, Please Try again.")
			continue
	else:
		print(f"You are logged in as {username}")
		return s, logged_in, username
	s.close()


def menu(s, logged_in, username):
	# once the user logs in this should give them options: Logout
	#TODO: implement this menu function when the user logs in 
	while not logged_in:
		print(f"What would you like to do {username}?")
	else:
		print("Please login")
		
		
def main():
	#TODO: fix logged_in make it its own function 
	# Start the application show menu with options
	print("Welcome to the App\n Menu: Login | Register | Exit")
	# Give the use the ability to choose from the options
	while True:
		menu_opt = input(">>").lower()
		if menu_opt == "login":
			# Establish the connection to the server using the socket
			s = establish_connection()
			login(s)
			break
		elif menu_opt == "exit":
			print("Bye See you soon!")
			sys.exit()
		else:
			print(f"{menu_opt} is not a valid menu option.")

			
if __name__ == "__main__":
    main()
