
import random
from component_node.Part_In import *
from component_node.Part_Out import *

leader_id= random.randint(1,100)
print('my id:',leader_id)
PORT_IN = int(sys.argv[1])
Have_Token = int(sys.argv[2])
Sd_Out = Part_Out()
Sd_In = Part_In(PORT_IN, Have_Token, Sd_Out)
Sd_In.start()
Sd_Out.port_next_neighbor = int(input("Numero de port voisin: "))
Sd_Out.start()