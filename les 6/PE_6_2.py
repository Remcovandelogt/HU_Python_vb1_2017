lijst=eval(input('geef lijst van minimaal 10 strings: '))
for woord in lijst:
    if len(woord)==4:
        print(woord,' ',end="")