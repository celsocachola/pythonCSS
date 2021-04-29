create table if not exists entradas (
  id integer primary key autoincrement,
  titulo string not null,
  texto string not null
);