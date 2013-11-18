import bitcoinrpc
from bitcoinrpc.exceptions import InsufficientFunds

conn = bitcoinrpc.connect_to_local()

try:
    conn.move("testaccount", "testaccount2", 1.0)
except InsufficientFunds,e:
    print "Account does not have enough funds available!"





info = conn.getinfo()
print "Blocks: %i" % info.blocks
print "Connections: %i" % info.connections
print "Difficulty: %f" % info.difficulty
