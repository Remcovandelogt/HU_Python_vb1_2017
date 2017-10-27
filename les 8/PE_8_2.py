import random
def monopolyworp():
    worp1=random.randint(1,6)
    worp2=random.randint(1,6)
    worp3=random.randint(1,6)
    worp4=random.randint(1,6)
    worp5=random.randint(1,6)
    worp6=random.randint(1,6)
    print('{} + {} = {}'.format(worp1,worp2,worp1+worp2))
    if worp1==worp2:
        print('{} + {} = {}'.format(worp3,worp4,worp3+worp4))
    elif worp3==worp4:
        print('{} + {} = {}'.format(worp5,worp6,worp5+worp6))
    elif worp5==worp6:
        print('Je moet naar de gevangenis!')
monopolyworp()