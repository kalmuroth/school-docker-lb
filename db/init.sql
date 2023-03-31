create database todo;
use todo;

CREATE TABLE tasks (
  title VARCHAR(20),
  completed VARCHAR(20)
);

INSERT INTO tasks
  (title, completed)
VALUES
  ('Task 1', 'Yes'),
  ('Task 2', 'No');
