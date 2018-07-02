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
		  
def initServer():
	s = socket.socket()
	s.bind(("127.0.0.1", 12345))
	s.listen(5)
	print('Server Listening...')
	print("Waiting for Connection")
	
	#establish a connection
	conn, addr = s.accept()
	print(f"Got connection from: {addr}")
	
	#collect username and password from client and decode them to pass it to validateLogin()
	username = conn.recv(1024).decode()
	password = conn.recv(1024).decode()
	login = validateLogin(username, password)
	conn.sendall(login.encode())
	
	
	#collect yes or no to logout from client then pass it to logout()
	response = conn.recv(1024).decode()
	Logout = logout(response)
	conn.sendall(Logout.encode())
	
	conn.close()
	
def validateLogin(username, password):
	if(username, password) in LOGINS:
		return "Success, Welcome! " + username
	else:
		return "Fail, please try again."

def logout(response):
	if response == ("yes") or response == ("Yes") or response == ("YES"):
		return "Logout successful, See you next time!"
	elif response == ("no") or response == ("No") or response == ("NO"):
		return "Logout unsuccessful, Thanks for sticking around!"
	else:
		return "Command not valid, try Yes or No"
	
initServer()	