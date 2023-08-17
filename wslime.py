import threading
from websockets.sync import server
import json


buf = ''

#yeet
def yeet(websocket):
  global buf
  websocket.send(buf) 
  buf = ''

def handler(websocket):
  global buf
  print('connected')
  yt = None
  while True:
    inp = input()
    buf += inp + '\n'
    if yt:
      yt.cancel()
    yt = threading.Timer(0.01, lambda: yeet(websocket))
    yt.start()
    

with server.serve(handler, 'localhost', 8001) as server:
  print('waiting for connection')
  server.serve_forever()
