#imports
import threading
import asyncio
from websockets.server import serve



buf = ''

#yeet
def yeet():
  global buf
  print(buf) 
  buf = ''

yt = None
while True:
  inp = input()
  buf += inp + '\n'
  if yt:
    yt.cancel()
  yt = threading.Timer(0.01, yeet)
  yt.start()



async def echo(websocket):
  await websocket.send(message) #here

async def main():
  async with serve(echo, "localhost", 8001):
    await asyncio.Future()  # run forever

asyncio.run(main())
