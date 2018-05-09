import csv
csv_list = dir(csv)

#print(csv_list)

with open('liz.csv','r') as c:
    r = csv.reader(c)
    for lines in r:
        print(lines[1])

with open('random.csv','w') as random:
    wr = csv.writer(random,delimiter=',')
    wr.writerow(['Elizabeth','Rosso'])
    wr.writerow(['Nora','Owen'])
    wr.writerow(['Emily','Walczak'])
    wr.writerow(['Matthew','Walczak'])
    wr.writerow(['Dylan','Owen'])

with open('random.csv','r') as c:
    r = csv.reader(c)
    for lines in r:
        print(lines)

with open('Liz.csv','r') as d:
    r = csv.DictReader(d)
    for rows in r:
        print(rows['language'])


with open('dict.csv','w') as dictf:
    f = ['firstname','lastname']
    wd = csv.DictWriter(dictf,fieldnames=f)
    wd.writeheader()
    wd.writerow({'firstname':'Elizabeth','lastname':'Rosso'})
    wd.writerow({'firstname': 'Nora', 'lastname': 'Owen'})

with open('dict.csv','r') as d:
    r = csv.DictReader(d)
    for rows in r:
        print(rows['firstname'])