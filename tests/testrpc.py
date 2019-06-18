import sys
print (sys.path)
import utils.rpc

url = "http://119.29.114.153:8545"
rpc = utils.rpc.HTTPProvider(url)
rpc.isConnected()
param=[1]

bn = rpc.make_request("getBlockNumber",param)
if "error" in bn:
    print("error %d, [%s]"%(bn["error"]["code"],bn["error"]["message"]))
else:
    print( int(bn['result'],16) )


txhash = "0x27a7e7c14470a534cbf491310d85ad8e5620a893637cc47cfac964413bb08bf9";
tx = rpc.make_request("getTransactionByHash",[1,txhash])
input  = tx["result"]["input"]
print (input)
