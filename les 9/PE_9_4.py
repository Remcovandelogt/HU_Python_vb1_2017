import csv

with open('headers.csv','w',newline='') as f:
    fieldnames=['artikelnummer','artikelcode','naam','voorraad','prijs']
    thewriter=csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    for i in range (0,1):
        thewriter.writerow({'artikelnummer':'121','artikelcode':'AB123','naam':'Highlight pen','voorraad':'231','prijs':'0.56'})
        thewriter.writerow({'artikelnummer':'123','artikelcode':'PQR678','naam':'Nietmachine','voorraad':'587','prijs':'9.99'})
        thewriter.writerow({'artikelnummer':'128','artikelcode':'ZYW163','naam':'Bureaulamp','voorraad':'34','prijs':'19.95'})
        thewriter.writerow({'artikelnummer':'137','artikelcode':'MLK709','naam':'Monitorstandaard','voorraad':'66','prijs':'32.50'})
        thewriter.writerow({'artikelnummer':'271','artikelcode':'TRS665','naam':'Ipad hoes','voorraad':'155','prijs':'19.01'})
with open('headers.csv') as csvfile:
    readCSV=csv.reader(csvfile, delimiter=',')
    prijs = []
    voorraad = []
    naam = []
    artikelcode = []
    artikelnummer = []
    for row in readCSV:
        prijs.append(row[4])
        voorraad.append(row[3])
        naam.append(row[2])
        artikelcode.append(row[1])
        artikelnummer.append(row[0])
prijs.remove('prijs')
voorraad.remove('voorraad')
naam.remove('naam')
artikelcode.remove('artikelcode')
artikelnummer.remove('artikelnummer')
print('Het duurste product is {} en kost {}'.format(naam[3],prijs[3]))
print('Slechts {} exmplaren van artikelnummer {} beschikbaar'.format(voorraad[2],artikelnummer[2]))
print('Er zijn {} produten in totaal op voorraad'.format(sum([231,587,34,66,155])))
