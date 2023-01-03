from lib import *

def Handle_Neighbor(con, add, t, sortie):
    while True:
        if t==0:
            msg=con.recv(1024)
            if msg.decode() == "TOKEN":
                print("Vous avez recu le token")
                print("vous avez le droit à la parole")
                print("Pour liberer la parole il faut saisir le mot token")
                while True:
                    expression=input("Vous pouvez vous exprimer : ")
                    if expression=="TOKEN":
                        break
        if t == 1:
            input("you are the first node tap enter")

        sortie.resume()
        t = 0


class Part_In(threading.Thread):
    def __init__(self, port, token, sd_out):
        threading.Thread.__init__(self)
        self.Sock_client = token
        self.port = port
        self.token = token
        self.ss = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.sd_out = sd_out
        try:
            self.ss.bind(('localhost', self.port))
        except:
            print("error in Part_In binding failed")
            sys.exit()
        self.ss.listen()
    def run(self):
        self.connexion, self.add = self.ss.accept()
        Handle_Neighbor(self.connexion, self.add, self.token, self.sd_out)