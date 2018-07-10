import socket
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
	s = establish_connection()
	login(s)


if __name__ == "__main__":
    main()
