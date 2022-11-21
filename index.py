from orjson import dumps
from websocket import create_connection
from time import time

link = "ws://127.0.0.1:8548"
ws = create_connection(link)
# old0xc59fBcdF5fea4c80fa4f1Ae2f20D51EF7B4472fc
gasFunc02 = str(dumps({
  "jsonrpc": "2.0",
  "id": 0,
  "method": "eth_getTransactionByHash01Pending",
  "params": [
    "pending"
  ]
}), "utf-8")
start = time() * 1000
ws.send(gasFunc02)
print(f"eth_getTransactionByHash01 tooks {(time()*1000) - start} ms, result ==  {ws.recv()}" )