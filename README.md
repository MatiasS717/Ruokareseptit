# Ruokareseptit

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään sovellukseen reseptejä. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään reseptejä.
- Käyttäjä näkee sovellukseen lisätyt reseptit. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät reseptit.
- Käyttäjä pystyy etsimään reseptejä hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä reseptejä.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät reseptit.
- Käyttäjä pystyy valitsemaan reseptille yhden tai useamman luokittelun, esim. alkuruoka, intialainen, vegaaninen. 
- Sovelluksessa on pääasiallisen reseptien lisäksi kommentit resepteihin. Käyttäjä pystyy lisäämään kommentteja omiin ja muiden käyttäjien resepteihin liittyen.

## Nykytilanne
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään sovellukseen reseptejä. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan reseptejä.
- Käyttäjä näkee sovellukseen lisätyt reseptit. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät reseptit.
- Käyttäjä pystyy etsimään reseptejä otsikon ja ainesosien perusteella.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät reseptit.
- Käyttäjä pystyy valitsemaan reseptille yhden tai useamman luokittelun.
- Käyttäjä pystyy lisäämään kommentteja omiin ja muiden käyttäjien resepteihin.
- Käyttäjä pystyy poistamaan omia kommenttejaan.

## Projektin käynnistäminen
Suorita seuraavat komennot komentorivissä hakemistossa Ruokareseptit.
### Luo Pythonin virtuaaliympäristö
`python3 -m venv venv`
### Aktivoi virtuaaliympäristö
`source venv/bin/activate`
### Asenna flask
`pip install flask`
### Luo tietokanta
`touch database.db`
### Alusta tietokanta
`sqlite3 database.db < schema.sql`

`sqlite3 database.db < init.sql`
### Käynnistä ohjelma
`flask run`
