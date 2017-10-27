import csv

with open('Gamers.csv')as csvfile:
    readCSV=csv.reader(csvfile, delimiter=',')
    name = []
    date = []
    score = []
    for row in readCSV:
        name.append(row[0])
        date.append(row[1])
        score.append(row[2])
    print('De hoogste score is: {} op {} behaald door {}'.format(max(score),date[5],name[5],))
