import socket
#TODO: add a loop to ask the user to have correct credentials 
#TODO: loop to return back to login once logged out 
#TODO: add registration 
#TODO: make PEP-8 Compliant

#Create a list of valid users and passwords
LOGINS = [("Alejandro", "pythonrules"),
		  ("Betty", "ilovethebackstreetboys"),
		  ("Maria", "postmalone"),
		  ("William", "pinkfloyd")
		  ]
		  
def initiate_Server():
	#Listen for connections
	s = socket.socket()
	s.bind(("127.0.0.1", 12345))
	s.listen(5)
	print('Server Listening...')
	print("Waiting for Connection")
	
	#keep server alive as long as user is trying to login
	user_logged_in = False
	
	if user_logged_in:
		conn.close()
	elif not user_logged_in:
		#establish a connection with the client.py
		conn, addr = s.accept()
		print(f"Got connection from: {addr}")
		msg = "A Connection has been established"
		conn.sendall(msg.encode())
		validate_Login(conn)
		conn.close()

def validate_Login(conn):
	#receive the input given by user to check if it is valid login
	username = conn.recv(1024).decode()
	password = conn.recv(1024).decode()
	
	if (username, password) in LOGINS:
		print("Success")
		rsp = f"Welcome! {username}"
	else:
		print("Failed")
		rsp = "Fail Try again"
	
	conn.sendall(rsp.encode())	
	conn.close()

def main():
	initiate_Server()

if __name__ == "__main__":
	main()	