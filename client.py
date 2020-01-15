from connection import Connection
from message import Message
from card import Card
from card_loader import CardLoader
from connection_manager import GameConnectionManager

'''
A class for handling the client side game connection.
'''
class GameClient(GameConnectionManager):

    def __init__(self, addr, cl : CardLoader):

        self.con = Connection()
        self.con.connect(addr)

        # get and process the "you are" message
        while True:

            msg = self.con.recieve()
            if msg:
                self.id = msg.get("your_id")
                super().__init__(list(msg.get("ids").split(",")))
                break

        # the id of the next player to get priority after this player
        self.next_id = self.ids[(self.ids.index(self.id) + 1) % len(self.ids)]

        self.card_loader = cl

    '''
    Tells the server that the given card was played.
    '''
    def send_card_played(self, card : Card, play_specs : str = "", keep_priority = False):

        msg = Message(
            type = "card_played",
            by = self.id,
            card = card.id,
            play_specs = play_specs,
            next_player = self.id if keep_priority else self.next_id
        )

        self.con.send(msg)

        self.handle(msg)

    def recieve(self):

        msg = self.con.recieve()
        if msg:
            self.handle(msg)
            return (self.card_loader.get_card(msg.get("card")), msg.get("play_specs"))

    '''
    Returns wether or not this player has priority.
    '''
    def has_prio(self):
        return self.get_prio_id() == self.id
