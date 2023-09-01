import path from 'path';
import url from 'url';
import express from 'express';
import { WebSocketServer } from 'ws';
import { createInterface } from 'readline';

const app = express()
app.listen(8000, () => {
  console.log('http server started');
});

app.use(express.static(process.cwd()));

app.get('/wslime', (req, res) => {
  const d = url.fileURLToPath(import.meta.url);
  res.sendFile(path.join(d, '../../wslime.js'));
});



let buf = ''
function yeet() {
  q.push(buf);
  msg = buf;
  buf = '';
}

let yt = null; // yeet timer

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on('line', input => {
  buf += input + '\n';
  if (yt) {
    clearTimeout(yt);
  }
  yt = setTimeout(yeet, 10);
});
