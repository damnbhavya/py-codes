import socket

def connect_to_google():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        google_ip = socket.gethostbyname('www.google.com')
        s.connect((google_ip, 80))
        print(f"Successfully connected to Google at IP: {google_ip}")

        request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
        s.sendall(request.encode())

        response = s.recv(4096)
        print("Received response from Google:", response.decode())

        s.close()
    except socket.error as err:
        print(f"Socket error: {err}")

connect_to_google()


