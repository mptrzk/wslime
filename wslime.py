import os
import threading
import queue
import argparse
from websockets.sync import server
from http.server import HTTPServer, SimpleHTTPRequestHandler


dir = os.path.dirname(__file__)
preset_dir = f'{dir}/static/presets'
cwd = os.getcwd()
client_name = 'wslime-client.js'

ap = argparse.ArgumentParser()
ag = ap.add_mutually_exclusive_group()
ag.add_argument('-i', '--init', nargs='?', const='default', metavar='preset')
ag.add_argument('-s', '--save-preset', metavar='preset')
ag.add_argument('-r', '--remove-preset', metavar='preset')
ag.add_argument('-l', '--list-presets', action='store_true', default=False)
args = ap.parse_args()

if args.init:
  os.system(f'cp -r {preset_dir}/{args.init}/* {cwd}')
  os.system(f'cp {dir}/static/{client_name} {cwd}')
  print('project initialized')
  exit(0)

if args.save_preset:
  p = f'{preset_dir}/{args.save_preset}'
  os.system(f'cp -r . {p}')
  os.system(f'rm {p}/{client_name}')
  print(f'preset saved at {p}')
  exit(0)

if args.remove_preset:
  p = f'{preset_dir}/{args.remove_preset}'
  os.system(f'rm -r {p}')
  exit(0)

if args.list_presets: 
  os.system(f'ls {preset_dir}') 
  exit(0)


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
