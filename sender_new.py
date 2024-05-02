import socket

def send_file(filename, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'FILE')
        with open(filename, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                s.sendall(data)

def main():
    host = '10.1.0.79'
    port = 12345
    filename = input("Enter the name of the file to send: ")
    send_file(filename, host, port)

if __name__ == "__main__":
    main()
