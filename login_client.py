import socket
import sys
"""
    TODO: Allow the user to logout and return to the option menu
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
        s.sendall("User:{}".format(username).encode())
        s.sendall("Password:{}".format(password).encode())
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
    return logged_in, username


def logout(s, logged_in, username):
    #TODO: Pass the variable login to create a user session here 
    # Allow the user to logout of the application
    while logged_in:
        print(f"Would you like to Logout {username}?")
        client_rsp = input("Yes or No >>").lower()
        if client_rsp == "yes":
            s.sendall(b"Logout")
            logout_rsp = s.recv(1024).decode()
            if "Success" in logout_rsp:
                print("You logged out successfully.\n See you soon!")
                return main()# Return user back to menu options
            else:
                print("Logout fail")
        else:
            print(f"{client_rsp} is not a valid response")
            break


def main():
    # Establish the connection to the server using the socket
    s = establish_connection()
    # Give the use the ability to choose from the options
    while True:
        # Start the application show menu with options
        print("Welcome to the App\n Menu: Login | Register | Exit")
        menu_opt = input(">>").lower()
        if menu_opt == "login":
            username, logged_in = login(s)
            logout(s, username, logged_in)
        elif menu_opt == "exit":
            print("Bye See you soon!")
            s.close()
            sys.exit()
        else:
            print(f"{menu_opt} is not a valid menu option.")


if __name__ == "__main__":
    main()
