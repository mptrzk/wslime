document.body.innerHTML = '';

function foo() {
  const bar = [1, 2, 3].map(x => x + ' Missisipi');
  document.body.innerHTML += bar.join(', ') + '<br>';
  return bar;
}
foo();

foo();
foo();
foo();

