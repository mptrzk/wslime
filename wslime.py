import threading
from websockets.sync import server
import json
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler


buf = ''

def yeet(websocket):
  global buf
  websocket.send(buf) 
  buf = ''

def handler(websocket):
  global buf
  print('connected')
  yt = None  #yeet timer
  while True:
    inp = input()
    buf += inp + '\n'
    if yt:
      yt.cancel()
    yt = threading.Timer(0.01, lambda: yeet(websocket))
    yt.start()

def wserve():
  global server
  with server.serve(handler, 'localhost', 8001) as server:
    print('waiting for connection')
    server.serve_forever()

threading.Thread(target=wserve, daemon=True).start()

h = partial(SimpleHTTPRequestHandler, directory='static')
HTTPServer(('localhost', 8000), h).serve_forever()

