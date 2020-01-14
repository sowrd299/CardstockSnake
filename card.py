'''
A superclass for representing cards.
Multiple copies of the same card should be represented by the same
card object.
'''
class Card():

    '''
    Takes the cards unique identifier.
    '''
    def __init__(self, i):
        self.id = i

    '''
    Returns the unique identifier of the card.
    '''
    def get_id(self):
        return self.id