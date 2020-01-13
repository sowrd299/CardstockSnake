from connection import ServerAcceptConnection

def main():

    con = ServerAcceptConnection()
    client_con = con.accept_client()

    while True:

        msg = client_con.recieve()
        if msg:
            print(msg)
            break

if __name__ == "__main__":
    main()