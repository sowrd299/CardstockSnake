from message import Message


'''
A superclass for game clients and servers.
'''
class GameConnectionManager():

    '''
    Takes a list of all ids in the game.
    '''
    def __init__(self, ids : [str]):

        self.ids = ids
        self.prio_id = self.ids[0]

    '''
    To be called after recieving any message.
    '''
    def handle(self, msg : Message):

        if msg.get("type") == "card_played":
            self.handle_card_played(msg)

    '''
    To be called after recieving a "card_played" message.
    '''
    def handle_card_played(self, msg : Message):

        self.prio_id = msg.get("next_player")

    '''
    Returns the id of the current player with priority.
    '''
    def get_prio_id(self):
        return self.prio_id