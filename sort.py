#every sorting algorithm will have its own function
import random as rand 





def insertionsort(a):

  for i in range(1, len(a)):
    val=a[i]

    j=i-1
    while j>=0 and val<a[j]:
      a[j+1]=a[j]
      j-=1
      
    a[j+1]=val
    


#####################


def bubblesort(a):
  for i in range(0,len(a)):
    for j in range(i,len(a)):
      #print(a[i],' ' ,a[j],"   ")
      if a[i]>a[j]:
        a[i],a[j]=a[j],a[i]
      


#####################################
def mergesort(a):
  if len(a)>1:

    m=len(a)//2

    left=a[:m]

    right=a[m:]

    mergesort(left)

    mergesort(right)

    k=i=j=0

    while i<len(left) and j<len(right):
      if left[i]<right[j]:
        a[k]=left[i]
        i+=1
        k+=1
      else:
        a[k]=right[j]
        j+=1
        k+=1
    
    while i<len(left):
      a[k]=left[i]
      k+=1
      i+=1

    while j<len(right):
      a[k]=right[j]
      j+=1
      k+=1


##########################


def quicksortleft(a, left, right ):
  if left< right:

    piv=partitionleft(a, left, right)

    quicksort(a, left, piv-1)

    quicksort(a, piv+1, right)


"""
def partitionr(a, left, right):
  pivot=rand.randint(left,right)#choosing a random pivot
  #pivot=right

  a[left],a[pivot]=a[pivot],a[left]#we put thr pivoit in the first place


  return partition(a,left,right)
"""
def partitionleft(a, left, right):
  pivot=left 
  #print("pivot is ",a[left],"   ")

  i=left+1

  for j in range(left+1, right+1):#we put the smaller elements to the left and the bigger one to the right
    if a[j]<=a[pivot]:
      a[i],a[j]=a[j],a[i]
      i+=1


  a[pivot],a[i-1]=a[i-1],a[pivot]
  pivot=i-1


  return pivot


#################################
#sorting with a pivot always in thw middle 

def quicksortmid(a, left, right ):
  if left< right:

    piv=partitionrmid(a, left, right)

    quicksortmid(a, left, piv-1)

    quicksortmid(a, piv+1, right)



def partitionrmid(a, left, right):
  pivot=(left+right)//2#choosing a random pivot
  #pivot=right

  a[left],a[pivot]=a[pivot],a[left]#we put thr pivoit in the first place


  return partitionmid(a,left,right)

def partitionmid(a, left, right):
  pivot=left 
  #print("pivot is ",a[left],"   ")

  i=left+1

  for j in range(left+1, right+1):#we put the smaller elements to the left and the bigger one to the right
    if a[j]<=a[pivot]:
      a[i],a[j]=a[j],a[i]
      i+=1


  a[pivot],a[i-1]=a[i-1],a[pivot]
  pivot=i-1


  return pivot 




#############################################

#with random pivot

def quicksort(a, left, right ):
  if left< right:

    piv=partitionr(a, left, right)

    quicksort(a, left, piv-1)

    quicksort(a, piv+1, right)



def partitionr(a, left, right):
  pivot=rand.randint(left,right)#choosing a random pivot
  #pivot=right

  a[left],a[pivot]=a[pivot],a[left]#we put thr pivoit in the first place


  return partition(a,left,right)

def partition(a, left, right):
  pivot=left 
  #print("pivot is ",a[left],"   ")


  i=left+1




  for j in range(left+1, right+1):#we put the smaller elements to the left and the bigger one to the right
    if a[j]<=a[pivot]:
      a[i],a[j]=a[j],a[i]
      i+=1



  a[pivot],a[i-1]=a[i-1],a[pivot]
  pivot=i-1


  return pivot 

##################################


def selectionsort(a):

  for i in range(0,len(a)):
    minin=i
    for j in range(i+1, len(a)):
      if a[j]<a[minin]:
        minin=j

    a[minin],a[i]=a[i],a[minin]


#############################


def countingsort(a, min, max):
  if min<0:
    freqN=(min+1)*[0]
    freqP=(max+1)*[0]
  else:
    freqN=[0]
    freqP=(max+1)*[0]
  
  for elem in a:
    if elem>=0:
      freqP[elem]+=1
    else:
      freqN[elem]+=1
  
  k=0

  for i in range(len(freqN),0):
    while freqN[i]>0:
      a[k]=i
      k+=1
      freqN[i]-=1

  for i in range(0,len(freqP)):
    while freqP[i]>0:
      a[k]=i
      k+=1
      freqP[i]-=1



###############################




def heapify(a, n, i):

  maxx=i
  l=2*i+1
  r=2*i+2

  if l<n and a[l]>a[maxx]:
    maxx=l

  if r<n and a[r]>a[maxx]:
    maxx=r

  if i!=maxx:
    a[i],a[maxx]=a[maxx],a[i]
    heapify(a,n,maxx)

def heapsort(a):
  n=len(a)

  for i in range(n//2,-1,-1):
    heapify(a,n,i)
  
  for i in range(n-1, 0, -1):
    a[i], a[0] = a[0], a[i]
    heapify(a, i, 0)

##################################

#uses insertion sort
#for numb betwewn 0 and 1
def bucketsort(a):

  bucket=[]

  for i in range(10):
    bucket.append([])


  for i in a:
    bucket[int(i*10)].append(i)

  for i in range(0,10):
    insertionsort(bucket[i])

  k=0

  for i in range(0, len(bucket)):
    for j in bucket[i]:
      a[k]=j
      k+=1

##########################

#uses insertion sort all numbers, 
# max has to be bigger than 100,min <-100 or 0
#and a multiple of 10
def bucketsort2(a,mini, maxi):

  bucket=[]

  for i in range(0, maxi+10, 10):
    bucket.append([])


  for i in a:
    bucket[int(i//10)].append(i)

  for i in range(0,maxi//10):
    insertionsort(bucket[i])

  k=0

  for i in range(0, len(bucket)):
    for j in bucket[i]:
      a[k]=j
      k+=1

########################################

#for radix sort
def countingsort2(a, exp):



  freqP=[[0] for i in range(10)]


  for elem in a:
    if exp!=1:param=(elem//(exp))% (exp //(exp//10))
    else:param=elem%10
    freqP[param][0]+=1
    freqP[param].append(elem)
    
  k=0

  for i in range(0,len(freqP)):
    j=1
    while freqP[i][0]>0:
      a[k]=freqP[i][ j]
      k+=1
      j+=1
      freqP[i][0]-=1


def radixsort(a):
  
  maxx=a[0]
  for i in a:
      if maxx<i:maxx=i

  exp=1
  while maxx//exp>0:
      countingsort2(a,exp)
      exp*=10





################################
###############################
#############################
############################


def issorted(a):
  for i in range(1,len(a)):
      if(a[i]<a[i-1]):return False
  return True




#list generators
















a=[2,34,5,43,2,24,43,2,32,23,33,3,2,2,23,3,32,32,32,32,32,23,23,2,11,45,55,67, 101]

b=[10,9,8,7,6,4,5,44,6,7,3,2,1]

#quicksortleft(a,0, len(a)-1)

#insertionsort(a)
#quicksort(a,0,len(a)-1)

c=[.34, .22, .77 , .33, .45 ,.455, .434,.9]

#bucketsort2(a,0,120)

#countingsort(a,0,500)

#for elem in a:
#  print(elem)

