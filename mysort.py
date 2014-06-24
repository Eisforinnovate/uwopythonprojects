# -*- coding: utf-8 -*-
#Part1: Get started
    #chosing heapsort
    #have to do two three things
    #1)impliment it in python
    #2)test implementation to make sure it works
    #3) write a brief description of how good you think the 
    #sorting alg is (how many loops does it have to do with n elements)
    #http://docs.python.org/2/library/heapq.html
    
    

from random import shuffle
pass_it = lambda x: x

def heappush(heap, item, key=pass_it):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1, key=key)

def _siftdown(heap, startpos, pos, key):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if key(parent) <= key(newitem):
            break
        heap[pos] = parent
        pos = parentpos
    heap[pos] = newitem

def _siftup(heap, pos, key):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
    if rightpos < endpos and key(heap[rightpos]) <= key(heap[childpos]): 
            childpos = rightpos
        # Move the smaller child up.
    heap[pos] = heap[childpos]
    pos = childpos
    childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos, key)

def heappop(heap, key=pass_it):
    """Pop the smallest item off the heap, maintaining the heap
invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0, key)
    else:
        returnitem = lastelt
    return returnitem

    
def heap_sort(a, count):
     #input: an unordered array a of length count
 
     #(first place a in max-heap order)
    heapify(a, count)
 
    end = count-1 
    #in languages with zero-based arrays the children are 2*i+1 and 2*i+2
    while end > 0:
         #(swap the root(maximum value) of the heap with the last element of the heap)
        swap(a[end], a[0])
         #(decrease the size of the heap by one so that the previous max value will
         #stay in its proper placement) 
        end = end - 1
         #(put the heap back in max-heap order)
    siftDown(a, 0, end)          
 
def heapify(a, count):
     #(start is assigned the index in a of the last parent node)
     start = (count - 2 ) / 2
     
     while start > 0:
         #(sift down the node at index start to the proper place such that all nodes below
         #the start index are in heap order)
         siftDown(a, start, count-1)
         start = start - 1
     #(after sifting down the root all nodes/elements are in heap order)
 
def siftDown(a, start, end):
     #input: end represents the limit of how far down the heap to sift.
     root = start

     while root * 2 + 1 < end:        
     #(While the root has at least one child)
         child = root * 2 + 1        
     #(root*2 + 1 points to the left child)
         swap = root        
         #(keeps track of child to swap with)
         #(check if root is smaller than left child)
     if a[swap] < a[child]:
             swap = child
         #(check if right child exists, and if it's bigger than what we're currently swapping with)
     if child+1 <= end and a[swap] < a[child+1]:
             swap = child + 1
         #(check if we need to swap at all)
     if swap != root:
            swap(a[root], a[swap])
            root = swap          
             #(repeat to continue sifting down the child now)
     else:
        return
             
#original heapsort used, was told in tutorial to try above   
#def heap_sort(iterable):
 #       'Equivalent to sorted(iterable)'
  #      h = []
   #     for value in iterable:
    #        heappush(h, value)
     #   return [heappop(h) for i in range(len(h))]
#testing heap with basic test 
def test_heap():
        lister=[2,1,0,4,6,5,7,9,8,10]
        test_dis = heap_sort(lister)
        print test_dis
        return test_dis
    
    #have to implement sorting based on someone else’s description
    
#part 2: data analytics
    #find your own dataset
    
    
    #going to 
    #1) pick a data set
    #http://archive.ics.uci.edu/ml/datasets/Bank+Marketing
    #2) figure out how to load in python
    #http://docs.python.org/2/library/csv.html

def load_data ():
    import csv
    with open('bank-full.csv',) as csvfile:  bank_data = csv.reader(csvfile)
            
    #3) do 2 different visualizations of the data, and interpret them
    #http://www.csd.uwo.ca/~jcamer7/CS2120/class11.html
    #http://matplotlib.org/gallery.html
#1 lines & bars
#http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html

def lines_bars():
    import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
#only numeric values in graph
bank_data = ('age','yearly balance', 'contact day', 'contact duration', 'contacts performed', 'pdays', 'number of contacts',) 
y_pos = np.arange(len(bank_data))
performance = np.random.rand(len(bank_data))
error = np.random.rand(len(bank_data))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, bank_data)
plt.xlabel('Performance')
plt.title('See the bank dada?')

plt.show()

#2 
#circles
#categorical
#http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html
import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 

plt.scatter(x, y, s=area, alpha=0.5)
plt.show()



# The slices will be ordered and plotted counter-clockwise.

    #4) Use two different machine learning approaches to analyze, 
    #and interpret your data.
#Visualization1, 4 features   
def data_set():
    import numpy
    from sklearn import datasets
    data_doe= datasets.bank_data()
    data = data_doe.data
    data.shape
    labels = bank_data.target
    numpy.unique(labels)
    
#Visualization 2
#Linear Support Vector Machine
def data_set_two():
    from sklearn import svm
    svc = svm.bank_data(kernel='linear')
    svc.fit(data,labels)
    #http://www.csd.uwo.ca/~jcamer7/CS2120/class14.html