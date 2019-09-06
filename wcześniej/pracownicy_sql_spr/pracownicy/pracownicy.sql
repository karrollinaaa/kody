DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy
(
    id_pracownika INTEGER PRIMARY KEY,
    nazwisko TEXT,
    kod TEXT,
    miasto_z TEXT,
    ulica TEXT,
    data_u DATE,
    miasto_u TEXT
);

DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty 
(
    id_pracownika INTEGER PRIMARY KEY,
    typ_k BOOLEAN,
    kontakt INTEGER,
    uwagi TEXT,
    FOREIGN KEY (id_pracownika) REFERENCES pracownicy(id_pracownika)
);

DROP TABLE IF EXISTS place;
CREATE TABLE place
(
    id_p INTEGER NOT NULL,
    id_s INTEGER,
    place INTEGER,
    data_z DATE,
    FOREIGN KEY (id_p) REFERENCES pracownicy(id_pracownika),
    FOREIGN KEY (id_s) REFERENCES pracownicy(id_stanowiska)
);

DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska 
(
    id_stanowiska INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT
);
