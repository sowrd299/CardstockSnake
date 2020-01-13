from connection import Connection

def main():
    
    con = Connection()
    con.connect("127.0.0.1")
    con.send("This is a test message")

if __name__ == "__main__":
    main()