/**
This is an init file.
Its contents are only meant to be loaded from a static file
and never sent over via slime.
**/
await Promise.all([
  wslime.load('foo.js'), //transparent module import
  import('./bar.js'), //EJS module import
]);

top.keepsies = 0;

await wslime.load('app.js');
