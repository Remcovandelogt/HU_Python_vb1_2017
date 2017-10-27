def read():
    file=open("Tickers.txt","r")
    d={}
    for line in file:
        x=line.split(":")
        a=x[0]
        b=x[1]
        c=len(b)-1
        b=b[0:c]
        d[a]=b
    print(d)
    company=input('Enter company name: ')
    print('Company sticker is: {}'.format(d[company]))
read()