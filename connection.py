import socket

PORT = 5006

'''
A superclass for socket connections.
'''
class Connection():

    terminator = "</msg>"

    def __init__(self, sock = None):

        self.socket = sock or socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.in_buffer = ""

    def connect(self, host):
        self.socket.connect((host, PORT))

    '''
    Sends the given string allong the connection.
    Assumes the message does not contain the terminator sequence.
    '''
    def send(self, msg : str):
        total_msg = msg + terminator
        total_sent = 0
        while total_sent < len(total_msg):
            sent = self.socket.send(total_msg[sent:])
            if sent == 0:
                raise RuntimeError("socket connection broken (found on send)")
            total_sent += sent

    def recieve(self):
        chunck = self.socket.recv(2048)
        if check == b'':
            raise RuntimeError("socket connection broken (found on recieve)")

'''
A class for connecting the server to accept connections with.
'''
class ServerAcceptConnection():

    max_clients = 2

    def __init__(self):

        super().__init__()
        self.socket.bind(('', PORT))
        self.socket.listen(self.max_clients)

    '''
    Accepts and manages a client. Returns after a client has connected.
    Returns the socket connection to that server.
    '''
    def accept_client(self):

        (client_socket, client_addr) = self.socket.accept()
        return Connection(client_socket)