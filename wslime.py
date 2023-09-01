import os
import threading
import queue
from bottle import run, route, static_file
from websockets.sync import server

cwd = os.getcwd()
script_dir = os.path.dirname(__file__)

@route('/')
def serve_index():
  return static_file('index.html', script_dir)

@route('/<filename:path>')
def serve_cwd(filename):
  return static_file(filename, cwd) 

@route('/wslime')
def serve_wslime():
  return static_file('wslime.js', script_dir)

def hserve():
  run(host='localhost', port=8000, debug=True)
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
