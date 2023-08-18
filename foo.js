document.body.innerHTML = '';

function foo() {
  const bar = [1, 2, 3];
  document.body.innerHTML += bar + '<br>';
  return bar;
}
foo();

foo();
foo();
foo();

