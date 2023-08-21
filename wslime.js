let fresh = true;
const init = cb => { 
  if (fresh) { //as event listener?
    cb();
    console.log('wslime: state initialized');
  }
}

console.log('waiting for wslime connection');
const ws = new WebSocket('ws://localhost:8001');
ws.onopen = () => console.log('wslime connected');
ws.onclose = () => console.log('wslime disconnected');
const indent = s => s.split('\n').map(x => '  ' + x).join('\n');


ws.onmessage = e => {
  fresh = false;
  let msg = indent(e.data.trim());
  msg = '>' + msg.slice(1);
  console.log(msg)
  let val = eval.apply(window, [e.data]);
  console.log(val)
}

export {init}
