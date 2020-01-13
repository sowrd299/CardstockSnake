from card import Card

'''
A superclass for systems that get cards by ID.
'''
class CardLoader():

    '''
    Gets a card by the given id.
    # TODO: Placeholder implementation.
    '''
    def get_card(self, id):
        return Card(id)