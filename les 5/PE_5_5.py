def gemiddelde():
    willekeurigezin = input('Doe maar wat')
    Allewoorden = willerkeurigezin.strip().split
    aantalwoorden = len(allewoorden)
    accumulator = 0
    for woord in allewoorden:
        accumulator += len(woord)
    print('gemiddelde lengte van de woorden in deze zin is: {}').format(accumulator/aantalwoorden)

gemiddelde ()
