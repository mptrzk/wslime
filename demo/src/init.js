/**
This is an init file.
Its contents are only meant to be loaded from a static file
and never sent over via slime.
It's purpose is to blah blah blah...
**/

await Promise.all([
  wslime.load('src/foo.js'), //transparent module import
  import('./lib/bar.js'), //EJS module import //leading dot?
]);

top.keepsies = 0;

await wslime.load('src/app.js');
