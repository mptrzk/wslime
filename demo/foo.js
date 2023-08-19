wslime.bufStart();

//make it look more idiomatic?
//wslime.onrefresh()?

//;i - init
wslime.init(() => {
  keepsies = 0;
});


  

//;C - clean
document.body.innerHTML = '';

//TODO make the DOM demo dependent on state
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

//I want refreshing state from vim, without reloading
//It should work in block eval and with buf eval if fresh

//Those are hacks around editor limitation, but I'd like to keep
//my editor simple
//TODO ponder tradeoffs
//it would be nice if I could reset state with something like ,B or ,R
// ,B - state reset
// ,R - page refresh
//
//another hack - commented block signifiers?
// &block
//  that would require wslime preprocessing stuff
// or maybe just keep stuff in different files?


if (!wslime.whole) {
  keepsies = 666;
}

console.log('keepsies:', keepsies++);

wslime.bufEnd();

