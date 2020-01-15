from client import GameClient
from card_loader import CardLoader

# for testing
import random

def main():
    
    cl = CardLoader() 
    client = GameClient("127.0.0.1", cl)
    while True:
        if client.has_prio():
            card = cl.get_card("{0}th Knight".format(random.randrange(1000)))
            client.send_card_played(card)
            print("Sent \"{0}\" card!".format(card.id))
        else:
            card, _ = client.recieve()
            print("Recieved \"{0}\" card!".format(card.id))

if __name__ == "__main__":
    main()