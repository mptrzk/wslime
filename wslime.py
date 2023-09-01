import sys
import os
import threading
import queue
import argparse
from websockets.sync import server
from http.server import HTTPServer, SimpleHTTPRequestHandler

dir = os.path.dirname(__file__)
cwd = os.getcwd()

ap = argparse.ArgumentParser()
ap.add_argument('--init', nargs='?', const='default')
args = ap.parse_args()

if args.init:
  os.system(f'cp -r {dir}/static/presets/{args.init}/* {cwd}')
  os.system(f'cp {dir}/static/wslime-client.js {cwd}')
  print('project initialized')
  sys.exit(0)


def hserve():
  h = SimpleHTTPRequestHandler
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
