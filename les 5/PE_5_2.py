def klantendbestand():
    infile=open('kaartnummers.txt','r')
    text=infile.readlines()
    infile.close()
    for mdw in text:
        regel=mdw.strip().split(', ')
        print("{} heeft kaarnummer: {}".format(regel[1], regel[0]))
klantendbestand()