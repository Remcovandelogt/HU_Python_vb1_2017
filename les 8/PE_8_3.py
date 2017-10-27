import random
def code():
    naam=input('Vul hier je naam in: ')
    beginstation=input('Vul hier je beginstation in: ')
    eindstation=input('Vul hier je eindstation in: ')
    for naam,beginstation,eindstation in range(0,100):
        print(naam,beginstation,eindstation)
code()