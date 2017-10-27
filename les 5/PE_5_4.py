import datetime

def registreertijd(hardloper):
    vandaag = datetime.datetime.today()
    s = vandaag.striftime("%a %d %b %Y %H %M %S")
    s+=', '+hardloper;
    outfile=open('hardopler.txt','a')
    outfile.write('s=\n')
    outfile.close()

def registreerhardloper():
    while True:
        hardlopernaam = input('Hoe heet deze hardloper?\n')
        if hardlopernaam == "":
            break
        registreertijd(hardlopernaam)