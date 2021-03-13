import numpy as np
import time
import timeit
import pickle
import csv
import random as rand
import sort
import list_generator as gen
import tracemalloc
import re
import multiprocessing
import gc
#https://docs.python.org/3/library/tracemalloc.html








#print([np.random.randint(0,999999,100000)])

'''
with open("1mili_usual.csv",'w') as f:
  writer=csv.writer(f)
  writer.writerows([np.random.randint(0,999999,1000000)])
'''

'''
with open("1mili_usual.csv",'r') as f:
  reader=csv.reader(f)
  li=list(reader)
  print(len(li))
'''



#with open('statistics.csv', 'a') as ff:
#    writer = csv.writer(ff)
#    writer.writerow(p)

#start=time.time()
#sort.heapsort(a)




with open("tempp.csv",'r') as f:
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
      if i==4:
        bb=e[i]
        print(bb)
        cc=float(bb)
        fff.append(cc)
      else:
        fff.append(e[i])

    li2.append(fff)

with open('temppp.csv', 'w') as ff:
    writer = csv.writer(ff)
    writer.writerows(li2)






a=''
g=gen.basicgenerator
f=sort.selectionsort#sortingalg
nr=100000
maxx=247483640
minn=0

#a=g(minn,maxx,nr)
filename="G2.csv"


try:
  with open(filename,'r') as fi:
    reader=csv.reader(fi)
    a=list(reader)
    a=list(map(int, a[0]))

except:
  with open(filename,'w') as fi:
    writer=csv.writer(fi)
    a=g(minn,maxx,nr)
    writer.writerow(a)
  first=0




#f=sort.mergesort



#auto={0:sort.heapsort,1:sort.bubblesort,2:sort.bucketsort2,3:sort.countingsort,4:sort.selectionsort,\
#5:sort.insertionsort,6:sort.mergesort,7:sort.quicksort,8:sort.radixsort}

auto={0:sort.heapsort,1:sort.bucketsort2,2:sort.countingsort,\
3:sort.mergesort,4:sort.quicksort,5:sort.radixsort}
#auto={0:sort.heapsort,1:sort.bubblesort,2:sort.bucketsort,3:sort.selectionsort,\
#4:sort.insertionsort,5:sort.mergesort,6:sort.quicksort}
#auto={0:sort.heapsort,1:sort.bucketsort,\
#2:sort.mergesort,3:sort.quicksort}


gc.enable()
for i in range(0,9):
  try:
    with open(filename,'r') as fi:
      reader=csv.reader(fi)
      a=list(reader)
      a=list(map(int, a[0]))

  except:
    with open(filename,'w') as fi:
      writer=csv.writer(fi)
      a=g(minn,maxx,nr)
      writer.writerow(a)
    first=0

  f=auto[i]

  tracemalloc.start()

  start=time.time()

  if auto[i]==sort.quicksort:
    auto[i](a,0,len(a)-1)

  else:
    if auto[i]==sort.bucketsort2 or auto[i]==sort.countingsort:
      auto[i](a,minn,maxx)

    else:
      auto[i](a)


  end=time.time()


  #print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

  snapshot = tracemalloc.take_snapshot()
  top_stats = snapshot.statistics("filename")
  #count==alocated memory blocks



  print(filename)
  print(g.__name__)
  print("Algorithm     ",f.__name__)

  print("time:      ",float(end-start),"sec")


  msize=re.search("size=.+?(?=,)",str(top_stats[0])).group(0)
  msize=msize[5:]
  print("Memory size      ",str(msize))

  print("numbers sorted    ",nr)
  print("min value      ",minn)
  print("max val     ",maxx)


  print("is sorted:    ", sort.issorted(a))

  #fields=['csv name','Generator','Algorithm','Time','Memory used','Numbers sorted','min val','max val','issorted']
  fields=[filename, g.__name__, f.__name__, float(end-start),"disabled",nr,minn,maxx,sort.issorted(a) ]
  with open('statistics0.csv', 'a') as ff:
      writer = csv.writer(ff)
      writer.writerow(fields)
  gc.collect()





