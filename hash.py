# my lib an valid and dict and list
import csv
lihash_filecsv = dict()
li =[]
lihash=[]
countname = 0
count_csv_hash = 0
d = 1
# read file csv for crack
locate = str(input('Type or Paste location file csv : '))
with open(locate) as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        d += 1
        for code in row[1:]:
            hashcode = code
            lihash_filecsv[name]=hashcode
            
a = list(lihash_filecsv.keys())
b = list(lihash_filecsv.values())
#creat password list
for pass_list in range(0,10000):
    count = pass_list
    hshing = str(pass_list).encode('utf-8')
    from hashlib import sha256
    t = sha256(hshing).hexdigest()

#if// for find password
    try :
        with open('E:\\Land program\\maktabkhooneh\\maktabkhooneh\\Begin\\Chapter6 (Project)\\2.csv') as s:
            reade_csv = csv.reader(s)
            for line_csv in reade_csv:
                if t == b[count_csv_hash]:
                    lihash.append(t)
                    lihash.append(count)
                    print('Number =>=> %i' % (countname+1))
                    print('Name =>=> %s' % a[countname])
                    print('Password =>=> %i' % count)
                    print('hash code =>=> %s' % t)
                    print('********************')
                    countname += 1
                    count_csv_hash += 1
    except :
        print('""WooooW"" These passwords for you :) ')
        break
