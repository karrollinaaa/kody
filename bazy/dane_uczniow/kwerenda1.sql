DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska 
(
    id_ucznia INTEGER PRIMARY KEY,
    Nazwisko TEXT(30),
    Pierwsze_imie TEXT(20),
    Drugie_imie TEXT
    
);
DROP TABLE IF EXISTS dane_osobowe;
CREATE TABLE dane_osobowe
(
    id_ucznia INTEGER,
	Dzien_urodzenia NOT NULL,
	Miesiac_urodzenia NOT NULL,
	Rok_urodzenia INTEGER PRIMARY KEY,
    Miejsce_urodzenia TEXT,
	FOREIGN KEY (id_ucznia) REFERENCES nazwiska(id_ucznia)
);
DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
    id_ucznia INTEGER,
	Zachowanie INTEGER DEFAULT NULL,
	Religia_etyka INTEGER DEFAULT NULL,
	Jezyk_polski INTEGER DEFAULT NULL,
    Jezyk_angielski INTEGER DEFAULT NULL,
    Jezyk_niemiecki INTEGER DEFAULT NULL,
    Matematyka INTEGER DEFAULT NULL,
    Historia INTEGER DEFAULT NULL,
    Geografia INTEGER DEFAULT NULL,
    Biologia INTEGER DEFAULT NULL,
    Fizyka INTEGER DEFAULT NULL,
    Chemia INTEGER DEFAULT NULL,
    Technika INTEGER DEFAULT NULL,
    Informatyka INTEGER DEFAULT NULL,
    Plastyka INTEGER DEFAULT NULL,
    PO INTEGER DEFAULT NULL,
    Wf TEXT,
	FOREIGN KEY (id_ucznia) REFERENCES nazwiska(id_ucznia)
);
