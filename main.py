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



#start=time.time()
#sort.heapsort(a)


a=''
g=gen.basicgenerator
f=sort.selectionsort#sortingalg
nr=10000
maxx=10000000
minn=0
#a=g(minn,maxx,nr)
filename="A1.csv"


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



auto={0:sort.heapsort,1:sort.bubblesort,2:sort.bucketsort2,3:sort.countingsort,4:sort.selectionsort,\
5:sort.insertionsort,6:sort.mergesort,7:sort.quicksort,8:sort.radixsort}
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

  if i==7:
    auto[i](a,0,len(a)-1)

  else:
    if i==2 or i==3:
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

  print("time:      ",end-start,"sec")


  msize=re.search("size=.+?(?=,)",str(top_stats[0])).group(0)
  msize=msize[5:]
  print("Memory size      ",str(msize))

  print("numbers sorted    ",nr)
  print("min value      ",minn)
  print("max val     ",maxx)


  print("is sorted:    ", sort.issorted(a))

  #fields=['csv name','Generator','Algorithm','Time','Memory used','Numbers sorted','min val','max val','issorted']
  fields=[filename, g.__name__, f.__name__, str(end-start)+"s","disabled",nr,minn,maxx,sort.issorted(a) ]
  with open('statistics.csv', 'a') as ff:
      writer = csv.writer(ff)
      writer.writerow(fields)
  gc.collect()







