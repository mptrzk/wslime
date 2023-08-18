import threading
import queue
from websockets.sync import server
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler


def hserve():
  h = partial(SimpleHTTPRequestHandler, directory='static')
  HTTPServer(('localhost', 8000), h).serve_forever()
threading.Thread(target=hserve, daemon=True).start()


q = queue.Queue()

def handler(websocket):
  print('connected')
  while True:
    try:
      msg = q.get()
      print('sending:')
      print(msg, end='')
      websocket.send(msg)
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


buf = ''

def yeet():
  global buf
  q.put(buf)
  buf = ''

yt = None  #yeet timer
while True:
  inp = input()
  buf += inp + '\n'
  if yt:
    yt.cancel()
  yt = threading.Timer(0.01, yeet)
  yt.start()
