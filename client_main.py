from connection import Connection

def main():
    
    con = Connection()
    con.connect("127.0.0.1")

    while True:

        msg = con.recieve()
        if msg:
            print(msg)
            break

if __name__ == "__main__":
    main()