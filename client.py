# import socket
# from ssl_protocol import ssl_handshake, SSLSocket
#
# # Create a socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Connect to the server
# s.connect(('localhost', 4444))
# print("Connected to server")
#
# # Perform SSL/TLS handshake with the server
# s_ssl = ssl_handshake('localhost', 4444)
#
# # Send data to the server
# s_ssl.sendall("Hello server, this is the client".encode())
#
# # Receive data from the server
# data = s_ssl.recv(1024)
# print(f"Received from server: {data.decode()}")
#
# # Close the connection
# s.close()
#-------------------------------------------------------------------
# import socket
# import ssl
#
# # Create a socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Connect to the server
# s.connect(('localhost', 4444))
# print("Connected to server")
#
# # Wrap the socket with an SSL context
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# context.load_verify_locations(cafile="server.crt")
# s_ssl = context.wrap_socket(s, server_hostname='localhost')
#
# # Send data to the server
# s_ssl.sendall("Hello server, this is the client".encode())
#
# # Receive data from the server
# data = s_ssl.recv(1024)
# print(f"Received from server: {data.decode()}")
#
# # Close the connection
# s_ssl.close()
#-------------------------------------------------------------------
import socket
import ssl

# get the hostname and initiate port
host = socket.gethostname() # as both code(server and client) is running on same pc
port = 4444

client_socket = socket.socket()
# connect to host address and port
client_socket.connect((host,port))

# wrap the socket in an SSL context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations('cert.pem')
ssl_connection = context.wrap_socket(client_socket,server_hostname=host)
# handshake
ssl_connection.do_handshake()

message = input('-->')
# send message to server
ssl_connection.send(message.encode())
# recive message from server
data = ssl_connection.recv(1024).decode()
print(f'server response: {data}')

ssl_connection.close()
print('\nconnection closed.')
















