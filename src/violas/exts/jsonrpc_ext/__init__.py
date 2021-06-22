import sys
import json
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../lbdiemclient/src/")))

from diem.jsonrpc import *
print("** this is " + __file__)
