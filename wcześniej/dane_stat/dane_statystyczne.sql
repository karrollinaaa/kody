DROP TABLE IF EXISTS miasta;
CREATE TABLE miasta 
(
    id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa_miasta TEXT(30),
    wojewodztwo TEXT(30)
    
);

DROP TABLE IF EXISTS powierzchnie;
CREATE TABLE powierzchnie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	powierzchnia_miasta DECIMALs,
	powierzchnia_terenow_zielonych DECIMAL,
    data aktualizacji DATE(10),
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_mista)
);

DROP TABLE IF EXISTS dane_gus;
CREATE TABLE dane_gus
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	liczba_mieszkancow INTEGER,
	liczba_kobiet INTEGER,
	grupa_wiekowa TEXT(10),
    data aktualizacji DATE(10),
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_mista)
);
