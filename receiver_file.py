import socket

def receive_file(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            if data == b'FILE':
                with open('received_file.txt', 'wb') as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                print("File received successfully.")

def main():
    host = '10.1.0.79'  # Receiver's IP address
    port = 12345
    receive_file(host, port)

if __name__ == "__main__":
    main()
