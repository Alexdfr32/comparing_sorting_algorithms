import numpy as np
import time
import timeit
import pickle
import csv
import random as rand
import sort
import tracemalloc
#https://docs.python.org/3/library/tracemalloc.html

#import .sort\



def basicgenerator(start,stop,steps):

  return np.random.randint(start,stop,steps).tolist()



def minilists(mainlist,start,stop,steps,nr):
  
  return [np.random.randint(start,stop,steps).tolist() for _ in range(nr)]

def sortedlist(size):
  return [i for i in range(size)]


def reversesorted(size):
  return [i for i in range(size,0)]


def floatlist(start,stop,size):
  return [rand.uniform(start,stop) for _ in range(size)]


def subunitarylists(size):
  return [rand.random for _ in range(size)]

def repetitive(size):
  return [rand.choice([1,2,3,4,5])]


def almostsorted(size):

  a=[i for i in range(size)]

  for i in range(5):
    r=rand.randint(1,size-1)
    a[r],a[r+1]=a[r+i],a[r]
  
  return a





