import csv

with open("statistics.csv",'r') as f:
  reader=csv.reader(f)
  li=list(reader)
  
  li2=[]
  ok=1
  for e in li:
    if ok==1:
      ok=0
      continue
    fff=[]
    for i in range(0,len(e)):
      print(e)
      if i==3:
        bb=e[i][:-1]
        print(bb)
        cc=float(bb)
        fff.append(cc)
      else:
        fff.append(e[i])

    li2.append(fff)

with open('statisticsnew.csv', 'w') as ff:
    writer = csv.writer(ff)
    writer.writerows(li2)
