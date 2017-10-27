def whileloop():
    getal = (int(input('vul hier je getal in: ')))
    while getal>0:
        print('Dit is niet nul')
        getal = (int(input('vul hier je getal in: ')))
        if getal==0:
            break
whileloop()
