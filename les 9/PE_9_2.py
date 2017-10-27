import csv

bestand = 'inloggers.csv'

def vraagOmInput ():
    while True:
        naam = input("Wat is je achternaam? ")
        break
    if naam == '':
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
    return naam,voorl,gbdatum,email

def schrijfWeg(naam,voorl,gbdatum,email):
    with open (bestand, 'a', newline='') as filetje:
        csvschrijver = csvwriter(filetje)
        csvschrijver.writerow(nowformatted(),naam,voorl,gbdatum,email)

vraagOmInput()