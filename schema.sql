DROP TABLE IF EXISTS Persons;
DROP TABLE IF EXISTS Works;
DROP TABLE IF EXISTS PersonsWorks;
DROP TABLE IF EXISTS Countries;
DROP TABLE IF EXISTS CountriesPersons;
DROP TABLE IF EXISTS CountriesWorks;
DROP TABLE IF EXISTS Types;
PRAGMA foreign_keys=on;

CREATE TABLE Persons (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    date_of_death TEXT
);

CREATE TABLE Types (
    type_id INTEGER NOT NULL PRIMARY KEY,
    type_name TEXT NOT NULL
);

CREATE TABLE Countries (
    id INTEGER NOT NULL PRIMARY KEY,
    country_name TEXT NOT NULL
);

CREATE TABLE Works (
    id INTEGER PRIMARY KEY NOT NULL,
    title TEXT NOT NULL,
    release_date INTEGER,
    type INTEGER,
    FOREIGN KEY (type) REFERENCES Types(type_id)
);

CREATE TABLE PersonsWorks (
    person_id INTEGER NOT NULL,
    work_id INTEGER NOT NULL,
    PRIMARY KEY (person_id, work_id),
    FOREIGN KEY (person_id) REFERENCES Persons(id),
    FOREIGN KEY (work_id) REFERENCES Works(id)
);

CREATE TABLE CountriesPersons (
    person_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    PRIMARY KEY (person_id, country_id),
    FOREIGN KEY (person_id) REFERENCES Persons(id),
    FOREIGN KEY (country_id) REFERENCES Countries(id)
);

CREATE TABLE CountriesWorks (
    work_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    PRIMARY KEY (work_id, country_id),
    FOREIGN KEY (work_id) REFERENCES Works(id),
    FOREIGN KEY (country_id) REFERENCES Countries(id)
);



