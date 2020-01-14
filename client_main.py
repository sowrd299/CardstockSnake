from client import GameClient
from card_loader import CardLoader

def main():
    
    cl = CardLoader() 
    client = GameClient("127.0.0.1", cl)
    while True:
        if client.has_prio():
            client.send_card_played(cl.get_card("Alpha Knight"))
            print("Sent card!")
        else:
            client.recieve()
            print("Recieved card!")

if __name__ == "__main__":
    main()