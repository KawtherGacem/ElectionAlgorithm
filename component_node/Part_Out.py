
from lib import *
class Part_Out(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.port_next_neighbor = 0
        self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.__flag = threading.Event()
        self.__flag.clear()

    def run(self):
        try:
            # self.ss.bind(('localhost', self.port))
            print(self.port_next_neighbor)
            self.s.connect(("localhost", self.port_next_neighbor))
        except:
            print("error in Part_Out binding failed")
            sys.exit()
        while True:
            self.__flag.wait()
            self.s.send(b"TOKEN")
            self.__flag.clear()

    def resume(self):
        self.__flag.set()