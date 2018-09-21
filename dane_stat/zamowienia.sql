DROP TABLE IF EXISTS zamowienia;
CREATE TABLE zamowienia 
(
    dane_zamowienia INTEGER PRIMARY KEY AUTOINCREMENT,
    IdKlient INTEGER,
    DataZamówienia DATE-TIME(30),
    WartZamNetto DECIMAL(10),
    WartZamBrutto DECIMAL(10),
    Vat % DECIMAL(5)
);

DROP TABLE IF EXISTS powierzchnie;
CREATE TABLE powierzchnie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	powierzchnia_miasta DECIMAL(20),
	powierzchnia_terenow_zielonych DECIMAL(20),
    data aktualizacji DATE(10),
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_mista)
);

DROP TABLE IF EXISTS dane_gus;
CREATE TABLE dane_gus
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	liczba_mieszkancow INTEGER(10),
	liczba_kobiet INTEGER(10),
	grupa_wiekowa TEXT(10),
    data aktualizacji DATE(10),
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_mista)
);
