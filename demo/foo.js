//;i - init
wslime.init(() => {
  keepsies = 0;
});


//;C - clean
document.body.innerHTML = '';

//TODO make the DOM demo dependent on state
//;f - foo
//vsmth?
//  naah, let's keep the demo 
function foo() {
  const bar = [1, 2, 3].map(x => x + ' Missisipi');
  document.body.innerHTML += bar.join(', ') + '<br>';
  return bar;
}
foo();

foo();
foo();
foo();


//note - even those labels add conceptual complexity
//;ck - clear keepsies

console.log('keepsies:', keepsies++);

wslime.bufEnd();

