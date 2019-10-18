DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie (
    id_ucznia CHAR(8) PRIMARY KEY,
    imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
    nazwisko VARCHAR(30) NOT NULL CHECK (nazwisko <> ''),
    klasa CHAR(5) DEFAULT ''
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nazwa VARCHAR(70) NOT NULL CHECK (nazwa <> '')
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    id_oceny INTEGER PRIMARY KEY AUTO_INCREMENT,
    data DATE NOT NULL,
    id_ucz CHAR(8),
    id_przedmiotu INTEGER,
    ocena DECIMAL(3,2),
    FOREIGN KEY (id_ucz) REFERENCES uczniowie(id_ucznia)
    ON DELETE CASCADE,
    FOREIGN KEY (id_przedmiotu) REFERENCES przedmioty(id)
    ON DELETE SET NULL
);
