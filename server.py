from connection import ServerAcceptConnection
from message import Message
from connection_manager import GameConnectionManager

'''
A class to manage a game server.
'''
class GameServer(GameConnectionManager):

    def __init__(self, num_players = 2):

        self.con = ServerAcceptConnection()
        self.players = dict()

        super().__init__([str(i) for i in range(num_players)])

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

    '''
    Will continue accepting players until all slots are filled.
    '''
    def accept_players(self):

        while len(self.players) < len(self.ids):
            self.accept_player()

    '''
    Recieves a message from the current client with priority,
    and forwards that to all other clients.
    '''
    def recieve_and_forward(self):

        # recieve the message
        prio_id = self.get_prio_id()
        msg = self.players[prio_id].recieve()

        # forward the message
        for player_id, player_con in self.players.items():
            if player_id != prio_id:
                player_con.send(msg)

        # handle the message
        self.handle(msg)


    def close(self):
        self.con.close()