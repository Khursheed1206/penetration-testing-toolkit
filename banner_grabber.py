import socket

def grab_http_banner(host, port):
    try:
        with socket.socket() as s:
            s.settimeout(2)
            s.connect((host, port))
            # Send a basic HTTP request
            http_request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(host)
            s.send(http_request.encode())
            banner = s.recv(1024).decode()
            return banner.split('\r\n')[0]  # Just show the HTTP response line
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    host = input("Enter host: ")
    port = int(input("Enter port: "))
    print(grab_http_banner(host, port))
