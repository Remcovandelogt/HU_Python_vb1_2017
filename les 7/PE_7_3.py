cijferscurus={'Bram':9,'Siem':8.5,'Jeroen':4.7,'Sam':4.7,'Stijn':6.4,'Anna':3.8,'Anne':9.5,'Sebastian':10}
def forloop():
    for key, value in cijferscurus.items():
        if value>9:
            print(key, value)
forloop()