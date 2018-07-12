import socket
"""
    TODO: Add logout validation to return success or failure logging off
"""
# create a list of valid users and passwords
LOGINS = [
    ("Alejandro", "pythonrules"),
    ("Betty", "ilovethebackstreetboys"),
    ("Maria", "postmalone"),
    ("William", "pinkfloyd")
]


def initiate_server():
    # Listen for connections
    s = socket.socket()
    s.bind(("127.0.0.1", 12345))
    s.listen(5)
    print('Server Listening...')
    print("Waiting for Connection")
    # establish a connection with the client.py
    conn, addr = s.accept()
    print(f"Got connection from: {addr}")
    msg = "A Connection has been established"
    conn.sendall(msg.encode())
    # check if the client is logged in or not
    logged_in = False
    while not logged_in:
        logged_in = validate_login(conn)
    return conn


def validate_login(conn):
    # receive the input given by user to check if it is valid login
    msg = conn.recv(1024).decode()
    command, username = msg.split(":")
    if command != "User":
        return False
    msg = conn.recv(1024).decode()
    command, password = msg.split(":")
    if command != "Password":
        return False
    if (username, password) in LOGINS:
        rsp = "Success"
        conn.sendall(rsp.encode())
        return True
    else:
        rsp = "Fail"
        conn.sendall(rsp.encode())
    return False


def logout(conn):
    # receive user input either yes or no to check for valid response
    received_rsp = conn.recv(1024).decode().lower()
    if received_rsp == "logout":
        conn.sendall(b"Success")
        return main()
        return True
    return False


def main():
    conn = initiate_server()
    logout(conn)
    conn.close()


if __name__ == "__main__":
    main()
