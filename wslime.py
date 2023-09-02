import os
import json
import threading
import queue
import argparse
from websockets.sync import server
from http.server import HTTPServer, SimpleHTTPRequestHandler



cwd = os.getcwd()
dir = os.path.dirname(__file__)
preset_dir = f'{dir}/static/presets'
client_name = 'wslime-client.js'
isproject = os.path.isfile(client_name)


ap = argparse.ArgumentParser()
ag = ap.add_mutually_exclusive_group()

ag.add_argument('-i', '--init', nargs='?', const='default', metavar='preset')
ag.add_argument('-u', '--update', action='store_true', default=False)
ag.add_argument('-s', '--save-preset', metavar='preset')
ag.add_argument('-r', '--remove-preset', metavar='preset')
ag.add_argument('-l', '--list-presets', action='store_true', default=False)

ap.add_argument('--hport', type=int, default=8000) 
ap.add_argument('--wport', type=int, default=8001) 

args = ap.parse_args()


def copy_client():
  os.system(f'cp {dir}/static/{client_name} {cwd}')

if args.init:
  #check if is a project, yaynay
  if isproject:
    print('directory already contains a wslime project')
  else:
    if args.init != 'minimal':
      os.system(f'cp -r {preset_dir}/{args.init}/* {cwd}')
    copy_client()
    print('project initialized')
  exit(0)

if args.update:
  if isproject:
    copy_client()
    print('client updated')
  else:
    print('directory doesn\'t contain a wslime project')
  exit(0)
  #check if is a project

if args.save_preset:
  if isproject:
    p = f'{preset_dir}/{args.save_preset}'
    os.system(f'cp -r . {p}')
    os.system(f'rm {p}/{client_name}')
    print(f'preset saved at {p}')
  else:
    print('directory doesn\'t contain a wslime project')
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
  HTTPServer(('localhost', args.hport), h).serve_forever()
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
  with server.serve(handler, 'localhost', args.wport) as server:
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
