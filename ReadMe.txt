Client-Server-Interactions

Welcome, this is a little project that connect the client to a server 
using python sockets to establish a connection.

Protocol:
	
	Client:
	USER:<username>
	PASSWORD:<password>
	
	Server:
	Success
	Fail

Requirements:

	Client:
		1. Login
			-Gather credentials from user
				-Ask user for username
			 	-Ask user for password
			-connect to the server	
			-Send the credentials to the server	
				-Send Username
				-Send Password
			-Receive response from server	
		2. Print response

	Server:
		1. Receive login from client
		2. Validate login
		3. Send result to client
			-send a string notifying the user his or her credentials are valid
			-send a string notifying the user his or her credentials are not valid

Other functions to be implemented:
1-Registration
	-Allow the user to create a new username and password 
2-Make PEP-8 Compliant
	-Since I am a new python noob make it, compliant with the 
	styling standards. 
