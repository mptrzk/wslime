document.body.innerHTML = '';

top.foo = () => {
  const bar = [1, 2, 3].map(x => x + ' Missisipi');
  document.body.innerHTML += bar.join(', ') + '<br>';
  return bar;
}
foo();

foo();
foo();
foo();

console.log('keepsies:', keepsies++);

