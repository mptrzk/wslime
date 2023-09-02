wslime = {
  attrib: s => document.querySelector('script').getAttribute(s),
  eval: async src => (async function (){}).constructor(src)(),
  load: async url => wslime.eval(await (await fetch(url)).text()),
};
wslime.ws = new WebSocket(`ws://localhost:${wslime.attrib('port') ?? 8001}`)


console.log('waiting for wslime connection');
wslime.ws = 
wslime.ws.onopen = () => console.log('wslime connected');
wslime.ws.onclose = () => console.log('wslime disconnected');


wslime.ws.onmessage = async e => {
  const indent = s => s.split('\n').map(x => '  ' + x).join('\n');
  let msg = indent(e.data.trim());
  msg = '>' + msg.slice(1);
  console.log(msg)
  let val = await wslime.eval(e.data);
  console.log(val)
}


wslime.load(wslime.attrib('init'));
