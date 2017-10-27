def woordlengte():
    woord =input('vul hier het woord in: ')
    while len(woord)>4:
        print('Dit woord heeft niet 4 letters')
        woord = input('vul hier het woord in: ')
        if woord == 4:
            break
woordlengte()
