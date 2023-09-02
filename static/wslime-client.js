(async () => {

  top.wslime = {
    eval: async src => (async function (){}).constructor(src)(),
    load: async url => wslime.eval(await (await fetch(url)).text()),
  };

  const config = (await (await fetch('config.json')).json())

  const ws = new WebSocket(`ws://localhost:${config.ws_port ?? 8001}`)


  console.log('waiting for wslime connection');
  ws.onopen = () => console.log('wslime connected');
  ws.onclose = () => console.log('wslime disconnected');


  ws.onmessage = async e => {
    const indent = s => s.split('\n').map(x => '  ' + x).join('\n');
    let msg = indent(e.data.trim());
    msg = '>' + msg.slice(1);
    console.log(msg)
    let val = await wslime.eval(e.data);
    console.log(val)
  }


  wslime.load(config.init);

})();
