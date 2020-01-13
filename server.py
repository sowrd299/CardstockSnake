from connection import ServerAcceptConnection
from message import Message

'''
A class to manage a game server.
'''
class GameServer():

    def __init__(self, num_players = 2):

        self.con = ServerAcceptConnection()
        self.players = dict()

        # explicitly for use establishing players
        self.ids = [str(i) for i in range(num_players)]

    '''
    Accepts and establishes a single player.
    '''
    def accept_player(self):

        client = self.con.accept_client()
        client_id = self.ids[len(self.players)]

        self.players[client_id] = client

        # send the "you are" message to establish id's
        client.send(Message(
            type = "you_are",
            your_id = client_id,
            ids = ",".join(self.ids)
        ))