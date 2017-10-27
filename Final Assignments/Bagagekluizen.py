def kluizen():
    open=infile('kluizen.txt','r')
    infile=read.readlines
    print('menuopties')
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn ')
    print('2: Ik wil een nieuwe kluis ')
    print('3: Ik wil even iets uit mijn kluis halen ')
    print('4: Ik geef mijn kluis terug')
    keuze=input('maak je keuze door het nummer in te geven!')
    if keuze==1:
     print('')