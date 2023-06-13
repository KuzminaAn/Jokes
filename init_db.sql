CREATE DATABASE project;

\c project;

CREATE TABLE Jokes (
        id            SERIAL PRIMARY KEY,
        user_id       INT NOT NULL,
        created_at    INT DEFAULT date_part('epoch', now())::int,
        content       TEXT,
        author        TEXT
);