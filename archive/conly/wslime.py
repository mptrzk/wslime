import os
import threading
from queue import Queue
from functools import partial
from websockets.sync import server
from http.server import HTTPServer, SimpleHTTPRequestHandler

def hserve():
  d = os.path.dirname(__file__)
  print(d)
  h = partial(SimpleHTTPRequestHandler, directory=d)
  HTTPServer(('localhost', 8000), h).serve_forever()
threading.Thread(target=hserve, daemon=True).start()

q = Queue()

def handler(ws):
  print('connected')
  while True:
    try:
      msg = q.get()
      ws.send(msg)
    except:
      print('disconnected')
      q.put(msg)
      break

def wserve():
  global server
  with server.serve(handler, 'localhost', 8001) as server:
    print('waiting for connection')
    server.serve_forever()
threading.Thread(target=wserve, daemon=True).start()

while True:
  q.put(input())
