letterlijst = ['a', 'b', 'c']
def wijzig(letterlijst):
    print(letterlijst)
    del letterlijst[0]
    del letterlijst[1]
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')
    del letterlijst[0]
    print(letterlijst)
wijzig(letterlijst)