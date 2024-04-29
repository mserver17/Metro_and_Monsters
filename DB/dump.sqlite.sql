-- TABLE
CREATE TABLE characters (
    character_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    job TEXT,
    town TEXT,
    strength INTEGER,
    agility INTEGER,
    endurance INTEGER,
    intelligence INTEGER,
    luck INTEGER
);
CREATE TABLE character_skills (
    character_id INTEGER,
    skill_id INTEGER,
    PRIMARY KEY (character_id, skill_id),
    FOREIGN KEY (character_id) REFERENCES characters (character_id),
    FOREIGN KEY (skill_id) REFERENCES skills (skill_id)
);
CREATE TABLE demo (ID integer primary key, Name varchar(20), Hint text );
CREATE TABLE skills (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name TEXT NOT NULL
);
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
