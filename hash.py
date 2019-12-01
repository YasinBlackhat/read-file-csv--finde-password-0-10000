# my lib an valid and dict and list
import csv
lihash_filecsv = dict()
li =[]
lihash=[]
countname = 0
count_csv_hash = 0
d = 1
# read file csv for crack
<<<<<<< HEAD
print('Example Type location : E:\\Land program\\new folder\\2.csv')
locat = str(input('Enter your location file csv : '))
with open(locat) as f:
=======
locate = str(input('Type or Paste location file csv : '))
with open(locate) as f:
>>>>>>> 5d2287294494f8125584f9bcc7d1c77a22306ef4
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
<<<<<<< HEAD

print('')
print('My Working End**')
            
                
            
            

=======
>>>>>>> 5d2287294494f8125584f9bcc7d1c77a22306ef4
