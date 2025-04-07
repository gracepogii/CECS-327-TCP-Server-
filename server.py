import socket
ip_address = "0.0.0.0"
port_number = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
server_socket.bind((ip_address, port_number))
server_socket.listen()
print(f"Server is listening on {ip_address}:{port_number}")
conn, addr = server_socket.accept()
with conn:
print(f"Connected to {addr}")
while True:
data = conn.recv(1024)
if not data:
break
response = data.decode().upper()
conn.sendall(response.encode())
