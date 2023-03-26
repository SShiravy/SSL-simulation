# import socket
# from ssl_protocol import ssl_handshake, SSLSocket
#
# # Create a socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Bind the socket to a local address and port
# s.bind(('localhost', 4444))
#
# # Listen for incoming connections
# s.listen()
#
# # Accept a connection from a client
# conn, addr = s.accept()
# print(f"Connection from {addr[0]}:{addr[1]}")
#
# # Perform SSL/TLS handshake with the client
# s_ssl = ssl_handshake('localhost', 4444)
#
# # Receive data from the client
# data = s_ssl.recv(1024)
# print(f"Received from client: {data.decode()}")
#
# # Send data to the client
# s_ssl.sendall("Hello client, this is the server".encode())
#
# # Close the connection
# conn.close()
#-------------------------------------------------------
# import socket
# import ssl
# # Create a socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Bind the socket to a local address and port
# s.bind(('localhost', 4444))
#
# # Listen for incoming connections
# s.listen()
#
# # Accept a connection from a client
# conn, addr = s.accept()
# print(f"Connection from {addr[0]}:{addr[1]}")
#
# # Wrap the socket with an SSL context
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain(certfile="server.crt", keyfile="server.key")
# conn_ssl = context.wrap_socket(conn, server_side=True)
#
# # Receive data from the client
# data = conn_ssl.recv(1024)
# print(f"Received from client: {data.decode()}")
#
# # Send data to the client
# conn_ssl.sendall("Hello client, this is the server".encode())
#
# # Close the connection
# conn_ssl.close()
#-------------------------------------------------------

import socket
import ssl
# get the hostname and initiate port
host = socket.gethostname()
port = 4444

server_socket = socket.socket()
# bind host address and port together
server_socket.bind((host,port))

# listen for clients and accept new connection
server_socket.listen()
connection,address = server_socket.accept()
print(f'server: connection from {str(address)}\n')

# wrap the socket in an SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='cert.pem',keyfile='key.pem')
ssl_connection = context.wrap_socket(connection,server_side=True)
# perform handshake
ssl_connection.do_handshake()


# receive data stream. it won't accept data packet greater than 1024 bytes
data = ssl_connection.recv(1024).decode()
print(f'connected user says: {str(data)}')
# send a message to client
ssl_connection.send('server recive your data'.encode())

ssl_connection.close()
print('\nconnection closed.')

















