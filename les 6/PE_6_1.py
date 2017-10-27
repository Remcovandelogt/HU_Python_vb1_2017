maand=['lente','zomer','herfst','winter']
def seizoen(maand):
    maandnummer=int(input('Vul hier het maandnummer in: '))
    if 3<=maandnummer<=5:
        print(maand[0])
    elif 11<=maandnummer>=9:
        print(maand[2])
    elif 11<maandnummer<3:
        print(maand[3])
    elif 5>maandnummer<9:
        print(maand[1])
seizoen(maand)