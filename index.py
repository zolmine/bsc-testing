from orjson import dumps
from websocket import create_connection
from time import time

link = "ws://127.0.0.1:8546"
ws = create_connection(link)
# gasFunc02 = str(dumps({
#   "jsonrpc": "2.0",
#   "id": 0,
#   "method": "eth_getBlockByNumber",
#   "params": [
#     "latest",
#     True
#   ]
# }), "utf-8")
# # gasFunc02 = str(dumps({
# #   "jsonrpc": "2.0",
# #   "id": 0,
# #   "method": "eth_getTransactionByHash01Pending",
# #   "params": [
# #     "pending"
# #   ]
# # }), "utf-8")
# start = time() * 1000
# ws.send(gasFunc02)
# print(f"GetTransactionsByBlockNumber tooks {(time()*1000) - start} ms, result ==  {ws.recv()}" )
gasFunc02 = str(dumps({
  "jsonrpc": "2.0",
  "id": 0,
  "method": "eth_getTransactionByBlockNumberAndIndex1",
  "params": [
    "pending"
  ]
}), "utf-8")
# gasFunc02 = str(dumps({
#   "jsonrpc": "2.0",
#   "id": 0,
#   "method": "eth_getTransactionByHash01Pending",
#   "params": [
#     "pending"
#   ]
# }), "utf-8")
start = time() * 1000
ws.send(gasFunc02)
print(f"GetTransactionsByBlockNumber1 tooks {(time()*1000) - start} ms, result ==  {ws.recv()}" )
