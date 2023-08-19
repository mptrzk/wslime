wslime.bufStart();

//make it look more idiomatic?
//wslime.onrefresh()?
if (wslime.fresh) {
  console.log('foo');
  keepsies = 0;
}
  

//;C - clean
document.body.innerHTML = '';

//;f - foo
function foo() {
  const bar = [1, 2, 3].map(x => x + ' Missisipi');
  document.body.innerHTML += bar.join(', ') + '<br>';
  return bar;
}
foo();

//;m - moar
foo();
foo();
foo();

//note - even those labels add conceptual complexity
//;ck - clear keepsies
if (!wslime.whole) {
  keepsies = 0;
}

//I want refreshing state from vim, without reloading
//It should work in block eval and with buf eval if fresh

//Those are hacks around editor limitation, but I'd like to keep
//my editor simple
//TODO ponder tradeoffs

keepsies++;


wslime.bufEnd();

