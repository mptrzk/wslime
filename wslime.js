wslime = {
  eval: async src => (async function (){}).constructor(src)(),
  load: async url => wslime.eval(await (await fetch(url)).text())
};


console.log('waiting for wslime connection');
const ws = new WebSocket('ws://localhost:8001');
ws.onopen = () => console.log('wslime connected');
ws.onclose = () => console.log('wslime disconnected');
const indent = s => s.split('\n').map(x => '  ' + x).join('\n');


ws.onmessage = async e => {
  fresh = false;
  let msg = indent(e.data.trim());
  msg = '>' + msg.slice(1);
  console.log(msg)
  let val = await wslime.eval(e.data);
  console.log(val)
}


window.onload = () =>
  [...document.querySelectorAll('script')]
  .filter(s => s.type === 'wslime')
  .forEach(async s => await wslime.load(s.src));
