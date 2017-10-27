def opdr():
    aantalkm=int(input('Hoeveel km moet je afleggen: '))
    if aantalkm>=50:
        print('je treinrit kost 15 euro + {} euro'.format(aantalkm*0.60))
    else:
        print('Treinrit kost {} euro'.format(aantalkm*0.80))
opdr()

def ritprijs():
    leeftijd=int(input('Wat is je leeftijd: '))
    weekendrit=input('reis je in het weekend(antwoord ja/nee):' )
    if weekendrit=='nee' and leeftijd<=12 or leeftijd>=65:
        print('Je reist met 30% korting!')
    elif weekendrit=='ja':
        print('je reist met 40% korting!')
ritprijs()
