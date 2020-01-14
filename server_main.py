from server import GameServer

def main():

    s = GameServer()
    s.accept_players()
    while True:
        s.recieve_and_forward()

if __name__ == "__main__":
    main()